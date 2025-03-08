import importlib
import logging

from robits.core.abc.robot import RobotBase
from robits.core.abc.gripper import GripperBase
from robits.core.abc.camera import CameraBase

from robits.core.config_manager import config_manager

logger = logging.getLogger(__name__)

class RobotFactory:
    """
    A factory class for building robot components such as grippers, cameras, and robots.

    This class provides methods to construct various components by loading configurations
    and dynamically importing and instantiating corresponding classes.
    """


    def build_gripper(self, config_name) -> GripperBase:
        """
        Builds and returns a gripper instance.

        :param config_name: Name of the gripper configuration.
        :return: An instance of the gripper.
        """
        return self.build_from_name("gripper", config_name)

    def build_camera(self, config_name) -> CameraBase:
        """
        Builds and returns a camera instance.

        :param config_name: Name of the camera configuration.
        :return: An instance of the camera.
        """
        return self.build_from_name("camera", config_name)

    def build_robot(self, config_name) -> RobotBase:
        """
        Builds and returns a robot instance.

        This method loads the robot configuration, constructs left and right arms if specified,
        and assigns grippers and cameras accordingly.

        :param config_name: Name of the robot configuration.
        :return: An instance of the robot.
        """        
        config_dict = config_manager.load_dict(config_name)


        for arm_side in [ "left_robot", "right_robot"]:
            if arm_side in config_dict:
                config = config_dict[arm_side]
                # ..todo:: also inject the side name
                #config["side_name"] = arm_side.split("_")[0]
                config_dict[arm_side] = self.build_robot(config)
        for config_type in ["gripper", "camera"]:
            if config_type in config_dict:
                config_dict[config_type] = self.build_from_name(config_type, config_dict[config_type])
        cameras = []
        if "cameras" in config_dict:
            for camera_name in config_dict["cameras"]:
                cameras.append(self.build_from_name("camera", camera_name))
        elif "camera" in config_dict:
            cameras.append(config_dict["camera"])                           
            config_dict.pop("camera")
        config_dict["cameras"] = cameras

        logger.info("building robot with config %s", config_dict)

        return self.build("robot", config_dict)
    
    def build_from_name(self, config_type, config_name: str):
        """
        Loads a configuration and builds an instance of the specified component type.

        :param config_type: The type of component to build (e.g., "gripper", "camera", "robot").
        :param config_name: The name of the configuration.
        :return: An instance of the specified component.
        """
        logger.info("Building %s from config %s", config_type, config_name)
        config_dict = config_manager.load_dict(config_name)
        return self.build(config_type, config_dict)
    
    def build(self, config_type, config_dict):
        """
        Dynamically imports and constructs a class instance from a configuration dictionary.

        :param config_type: The type of component to build.
        :param config_dict: The configuration dictionary.
        :return: An instance of the specified class.
        """
        if not "class_path" in config_dict:
            logger.error("Unable to determine class path.")
            return None
        class_path = config_dict["class_path"]
        config = config_manager.from_dict(config_type, config_dict)

        module_name, class_name = class_path.rsplit('.', 1)
        m = importlib.import_module(module_name)
        cls = getattr(m, class_name)
        args = config.__dict__.copy()
        args.update(args.pop("kwargs"))        
        return cls(**args)
