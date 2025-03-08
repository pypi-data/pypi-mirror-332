from abc import ABC
from abc import abstractmethod

from typing import Dict
from typing import Any
from typing import Tuple

from importlib.resources import open_text

from functools import lru_cache
import json

import numpy as np


from robits.core.data_model.camera_capture import CameraData
from robits.config import camera_data



class CameraBase(ABC):


    camera_name: str

    def __str__(self):
        return f"{self.camera_name}"

    def is_complete(self):
        """
        Checks if the camera node has received camera images
        """
        pass

    def is_wrist_camera(self) -> bool:
        """
        :returns: True if the camera is mounted to a robot
        """
        return False

    @abstractmethod
    def get_camera_data(self) -> Tuple[CameraData, Dict[str, Any]]:
        """
        Blocks until the camera images are complete and returns them

        :returns: the camera images and metadata
        """
        pass
    

    def request_capture(self) -> None:
        """
        Clears the camera data
        """
        pass

    @property
    @lru_cache()
    def extrinsics(self) -> np.ndarray:
        """
        :returns: the extrinsic parameters of the camera
        """
        resource = f"{self.camera_name}_camera_extrinsics.json"

        with open_text(camera_data, resource) as file:
            return np.array(json.load(file))


    @lru_cache()
    def updated_intrinsics(self, target_image_size):
        """
        :param target_image_size: the width x height of the new resolution
        """

        from robits.utils.vision_utils import resize_intrinsics

        intrinsics = self.intrinsics
        camera_data, metadata = self.get_camera_data()
        depth_image = camera_data.depth_image

        return resize_intrinsics(intrinsics, depth_image.shape, target_image_size)


    @property
    @lru_cache()
    def intrinsics(self) -> np.ndarray:
        """
        :returns: the intrinsic parameters of the camera
        """

        # ..todo:: store the camera_name as well as the resolution
        #..todo:: use config_manager


        resource = f"{self.camera_name}_camera_intrinsics_640x480.json"

        with open_text(camera_data, resource) as file:
            return np.array(json.load(file))



    def get_camera_info(self) -> Dict[str, Any]:
        return self.metadata.get(self.camera_name)

