from typing import Dict
from typing import Any
from typing import Optional
from typing import Sequence

import json

from dataclasses import dataclass
from dataclasses import _MISSING_TYPE
from dataclasses import field

import numpy as np

@dataclass(frozen=True)
class BaseConfig:
    """
    A basic configuration. 
    Additional parameters are stored in a kwargs dictionary.
    """

    def __init__(self):
        self.kwargs = {}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """
        Initializes the class from a Dict
        """

        parameter_keys = cls.__dataclass_fields__.keys()
        default_parameters = cls.get_default_parameters()
        default_parameters.update({k: v for k,v in data.items() if k in parameter_keys})
        other_parameters = {k: v for k,v in data.items() if not k in parameter_keys}
        
        instance = cls(**default_parameters)
        instance.kwargs.update(other_parameters)
        
        return instance

    @classmethod
    def get_default_parameters(cls) -> Dict[str, Any]:
        return {k: v.default
                for k, v in cls.__dataclass_fields__.items()
                if not isinstance(v.default, _MISSING_TYPE)}


    def save_config(self, config_path) -> None:
        """
        Serializes the current state

        :param config_path: the path to serialize to
        """
        with open(config_path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the class to a dictionary
        """
        data = self.config.__dict__.copy()
        data.uppdate(data.pop("kwargs"))
        return data

    def to_json(self) -> None:
        json.dumps(self.to_dict(), indent=4)
    


@dataclass(frozen=True)
class MainConfig(BaseConfig):

    min_scene_bounds: Optional[Sequence[float]] = field(default_factory=lambda: [0.2, -0.4, 0.30])
    max_scene_bounds: Optional[Sequence[float]] = field(default_factory=lambda: [0.62, 0.4, 0.70])

@dataclass(frozen=True)
class CameraConfig(BaseConfig):

    """
    Configuration class for a camera.

    :param camera_name: Name of the camera.
    :param width: Image width in pixels (default: 640).
    :param height: Image height in pixels (default: 480).
    :param hz: Frame rate in Hertz (default: 30).
    :param rgb: Whether RGB images are enabled (default: True).
    :param depth: Whether depth images are enabled (default: True).
    :param point_cloud: Whether point cloud data is enabled (default: True).
    :param kwargs: Additional configuration parameters.
    """

    camera_name: str

    width: int = 640

    height: int = 480

    hz: int = 30

    rgb: bool = True
    depth: bool = True
    point_cloud: bool = True

    kwargs: Dict[str, Any] = field(default_factory=lambda: {})


@dataclass(frozen=True)
class RobotConfig(BaseConfig):

    """
    Configuration class for a robot.

    :param robot_name: Name of the robot.
    :param default_joint_positions: The joint positions for the home pose (default: None).
    :param joint_names: Names of the joints (default: None).
    :param gripper: Gripper configuration (default: None).
    :param cameras: List of camera configurations (default: None).
    :param transform_robot_to_world: 4x4 matrix of the root  in world coordinates
    :param kwargs: Additional configuration parameters.
    """

    robot_name: str

    default_joint_positions: Optional[Sequence[float]] = None

    joint_names: Optional[Sequence[str]] = None

    gripper: Optional[Any] = None

    cameras: Optional[Sequence[Any]] = None

    transform_robot_to_world: np.ndarray = field(default_factory=lambda: np.identity(4)) 

    kwargs: Dict[str, Any] = field(default_factory=lambda: {})


@dataclass(frozen=True)
class GripperConfig(BaseConfig):
    """
    Configuration class for a gripper.

    :param gripper_name: Name of the gripper.
    :param kwargs: Additional configuration parameters.
    """

    gripper_name: str
    kwargs: Dict[str, Any] = field(default_factory=lambda: {})


@dataclass(frozen=True)
class AudioConfig(BaseConfig):
    """
    Configuration class for audio settings.

    :param kwargs: Additional configuration parameters.
    """

    audio_backend_name: str = ""

    kwargs: Dict[str, Any] = field(default_factory=lambda: {})


@dataclass(frozen=True)
class SpeechConfig(BaseConfig):
    """
    Configuration class for speech settings.

    :param kwargs: Additional configuration parameters.
    """

    speech_backend_name: str = ""

    player: str = ""

    cache_path: str = ""

    kwargs: Dict[str, Any] = field(default_factory=lambda: {})
