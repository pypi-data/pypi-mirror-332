from abc import ABC
from abc import abstractmethod

from typing import Dict
from typing import Any
from typing import List
from typing import Tuple

from functools import wraps

import logging

import numpy as np

from robits.core.abc.camera import CameraBase

from robits.utils import vision_utils

logger = logging.getLogger(__name__)


def check_bounds():

    def decorator(func):

        @wraps(func)
        def wrapper(self, action, **kwargs):

            #min_bounds = np.array([0.2, -0.4, 0.41])
            min_bounds = np.array([0.2, -0.4, 0.30])
            max_bounds = np.array([0.62, 0.4, 0.70])

            if np.any(action.position < min_bounds):
                logger.warning("out of bounds")
                return False
            if np.any(action.position > max_bounds):
                logger.warning("out of bounds")
                return False
            else:
                return func(self, action, **kwargs)

        return wrapper

    return decorator



class Perception:
    """
    ..todo:: this should by async and return a future
    """

    cameras: List[CameraBase]

    default_resolution = None

    def request_vision_data(self):
        """
        Clears all current cameras buffers
        """
        for camera in self.cameras:
            camera.request_capture()

    def has_vision_data(self) -> bool:
        """
        Indicates weather the cameras has captured an image

        ..todo:: use a timestamp to check if the age of the image
        """
        for camera in self.cameras:
            if not camera.is_complete():
                return False
        return True


    def set_default_camera_resolution(self, target_image_size: Tuple[int, int]):
        self.default_resolution = target_image_size


    def get_vision_data(self, include_point_cloud: bool=False, swap_channels:bool=False) -> Dict[str, np.ndarray]:
        """
        Returns all the vision data
        """

        obs = {}

        for camera in self.cameras:
            camera.request_capture()

        for camera in self.cameras:
            camera_name = camera.camera_name


            camera_data, _medatadata = camera.get_camera_data()
            intrinsics = camera.intrinsics

            depth_image = camera_data.depth_image
            rgb_image = camera_data.rgb_image

            logger.debug("RGB image has shape %s", rgb_image.shape)

            obs[f"{camera_name}_camera_extrinsics"] = camera.extrinsics
            obs[f"{camera_name}_camera_intrinsics"] = intrinsics

            if swap_channels:
                # c x w x h
                obs[f"{camera_name}_rgb"] = rgb_image.transpose((2, 1, 0))
            else:
                # h x w x c
                obs[f"{camera_name}_rgb"] = rgb_image
                
            # h x w    

            logger.debug("RGB image has shape %s", obs[f"{camera_name}_rgb"].shape)

            obs[f"{camera_name}_depth"] = depth_image

            logger.debug("Depth image has shape %s", obs[f"{camera_name}_depth"].shape)

            if include_point_cloud:

                pcd = vision_utils.depth_to_pcd(camera_data, camera, apply_extrinsics=True)
                point_cloud = np.asarray(pcd.points)

                if swap_channels:
                    # c x h x w
                    obs[f"{camera_name}_point_cloud"] = point_cloud.transpose((2, 1, 0))
                else:
                    obs[f"{camera_name}_point_cloud"] = point_cloud


                logger.info("Point cloud has shape %s", obs[f"{camera_name}_point_cloud"].shape)
           
        return obs



class RobotBase(ABC):


    @abstractmethod
    def get_obs(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def has_proprioception_data(self) -> bool:
        pass

    @abstractmethod
    def get_proprioception_data(self) -> Dict[str, Any]:
        pass

    def request_proprioception_data(self):
        pass

    @property
    def eef_pose(self):
        pass

    @property
    def eef_matrix(self):
        pass
    

class UnimanualRobot(Perception):

    robot_name = "robot"

    def get_obs(self)  -> Dict[str, Any]:
        """
        Also updates extrinsics parameters for wrist cameras
        """
        obs = {}

        obs.update(self.get_vision_data())
        obs.update(self.get_proprioception_data())

        gripper_matrix = obs["gripper_matrix"]
        m = np.linalg.inv(gripper_matrix)
        for camera in self.cameras:
            if camera.is_wrist_camera():
                extrinsics = obs[f"{camera.camera_name}_camera_extrinsics"]
                obs[f"{camera.camera_name}_camera_extrinsics"] = np.dot(extrinsics, m)
        
        return obs

    def has_data(self):
        return self.has_vision_data() and self.has_proprioception_data()

    def request_data(self):
        self.request_vision_data()
        self.request_proprioception_data()



class BimanualRobot(Perception):

    def __init__(self, right_robot: RobotBase, left_robot: RobotBase, **kwargs):
        print("!", kwargs)
        self.left_robot = right_robot
        self.right_robot = left_robot

        #self.control = BimanualControlManager(right_robot.control, left_robot.control)

    def get_obs(self)  -> Dict[str, Any]:
        obs = {}
        obs.update(self.get_vision_data())
        obs.update({f"right_{k}": v for k,v in self.right_robot.get_proprioception_data().items()})
        obs.update({f"left_{k}": v for k,v in self.left_robot.get_proprioception_data().items()})

        #..todo:: handle extrinsics

        return obs

    def has_data(self):
        return self.has_vision_data() and self.right_robot.has_proprioception_data() and self.left_robot.has_proprioception_data()
   
    def request_data(self):
        self.request_vision_data()
        self.right_robot.request_proprioception_data()
        self.left_robot.request_proprioception_data()


class DummyRobot(UnimanualRobot):


    def __init__(self, gripper, cameras: List[CameraBase], audio=None, speech=None, **kwargs): 
        self.gripper = gripper
        self.cameras = cameras
        self.audio = audio
        self.speech = speech

    @property
    def eef_pose(self):
        return np.zeros(3), np.array([0, 0, 0, 1])

    @property
    def eef_matrix(self):
        return np.identity(4)
