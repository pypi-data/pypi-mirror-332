from typing import List
from typing import Dict
from typing import Any
from typing import Sequence

from abc import ABC
from abc import abstractmethod

import json
import os
from pathlib import Path
from functools import lru_cache


from importlib.resources import contents as files
from importlib.resources import path
from importlib.resources import is_resource

from robits.core import config as config_module
from robits.core.config import BaseConfig
from robits.core.config import MainConfig

from robits.config import robot as robot_config_package
from robits.config import gripper as gripper_config_package
from robits.config import camera as camera_config_package
from robits.config import audio as audio_config_package
from robits.config import speech as speech_config_package


class ConfigFinder(ABC):

    @abstractmethod
    def find_config(self, config_name: str) -> Path:
        """
        Get the full path of a JSON configuration file. If a config cannot be found, None is returned. 

        :param config_name: Name of the config file (without extension).
        :return: Path object representing the full path to the JSON config file.
        """
        pass


    @abstractmethod
    def list(self) -> Sequence[str]:
        """
        Lists available configurations.

        :returns: A list of available configuration names.
        """
        pass


    @abstractmethod
    def name(self) -> str:
        """
        Name of the config finder
        """
        pass

    @abstractmethod
    def path(self) -> Path:
        """
        Root path the ConfigFinder operates in 
        """
        pass



class PackageResourceFinder(ConfigFinder):
    """
    Searches for json configs inside a given package
    """

    def __init__(self, package):
        self.package = package
    
    def find_config(self, config_name: str) -> Path:
        resource = f"{config_name}.json"
        if not is_resource(self.package, resource):
            return None
        with path(self.package, resource) as resource_path:
            return resource_path

    def list(self) -> List[str]:
        return [s[:-5] #os.path.splitext(s)[0]
                for s in files(self.package) 
                if s.endswith(".json")]

    @property
    def name(self) -> str:
        return self.package.__name__.rsplit(".")[-1]
    
    @property
    def path(self) -> Path:
        return Path(self.package.__path__[0])



class WorkspaceConfigFinder(ConfigFinder):
    """
    Searches for configs inside a folder
    """

    def __init__(self):
        config_dir = os.environ.get("ROBITS_CONFIG_DIR")
        self.config_dir = Path(config_dir).resolve()

        if not self.config_dir.is_dir():
            raise ValueError(f"Invalid configuration directory: {self.config_dir}")

    def find_config(self, config_name: str) -> Path:
        config_path = self.config_dir / f"{config_name}.json"
        if not config_path.exists():
            return None
        return config_path

    def list(self) -> List[str]:         
        return [p.stem for p in self.config_dir.glob("*.json")]
    
    @property
    def name(self) -> str:
        return self.config_dir.basename()

    @property
    def path(self) -> Path:
        return self.config_dir



class ConfigManager:
    """
    Manages configuration files for different hardware components such as robots, grippers, cameras,
    audio backends, and speech backends. Provides methods to retrieve configuration paths, load configurations,
    and list available configurations.
    """

    def __init__(self):
        self.meta_path = []
        if os.environ.get("ROBITS_CONFIG_DIR"):
            self.meta_path.append(WorkspaceConfigFinder())
        self.meta_path.append(PackageResourceFinder(robot_config_package))
        self.meta_path.append(PackageResourceFinder(gripper_config_package))
        self.meta_path.append(PackageResourceFinder(camera_config_package))
        self.meta_path.append(PackageResourceFinder(audio_config_package))
        self.meta_path.append(PackageResourceFinder(speech_config_package))

    def main_config(self) -> MainConfig:
        return MainConfig()

    def get_config_path(self, config_name: str) -> Path:
        """
        Retrieves the file path of a configuration file.

        :param config_name: The name of the configuration.
        :returns: The full path to the configuration file.
        """
        for finder in self.meta_path:
            if path := finder.find_config(config_name):
                return path
                
    def load_dict(self, config_name: str) -> Dict[str, Any]:
        """
        Loads a configuration file as a dictionary.

        :param config_name: The name of the configuration.
        :returns: The configuration data.
        """
        for finder in self.meta_path:
            if path := finder.find_config(config_name):
                with path.open("r", encoding="utf-8") as file:
                    return json.load(file)       

    def from_dict(self, config_type: str, config: Dict[str, Any]) -> BaseConfig:
        """
        Converts a dictionary into a configuration object of the appropriate type.

        :param config_type: The type of configuration.
        :param config: The configuration dictionary.
        :returns: An instance of the appropriate configuration class.
        """
        config_class_name = {
            "camera": "CameraConfig",
            "robot": "RobotConfig",
            "gripper": "GripperConfig",
            "speech": "SpeechConfig",
            "audio": "AudioConfig"
        }
        class_name = config_class_name[config_type]
        cls = getattr(config_module, class_name)
        return cls.from_dict(config)

    @lru_cache()
    def list(self) -> List[str]:
        """
        Lists all available configurations

        :returns: A list of available configuration names.
        """
        config_names = []
        for finder in self.meta_path:
            config_names.extend(finder.list())
        return config_names
    
    @property
    def available_robots(self) -> List[str]:
        """
        Retrieves a list of available robot configurations.

        :returns: Available robot configuration names.
        """
        return [n for n in self.list() if n.startswith("robot_")]
    

    @property
    def available_bimanual_robots(self) -> List[str]:
        """
        Retrieves a list of available bimanual robot configurations.

        :returns: Available bimanual robot configuration names.
        """
        return [n for n in self.list() if n.startswith("robot_") and "bimanual" in n]
    
    
    @property
    def available_grippers(self) -> List[str]:
        """
        Retrieves a list of available gripper configurations.

        :returns: Available gripper configuration names.
        """
        return [n for n in self.list() if n.startswith("gripper_")]
    
    @property
    def available_cameras(self) -> List[str]:
        """
        Retrieves a list of available camera configurations.

        :returns: Available camera configuration names.
        """
        return [n for n in self.list() if n.startswith("camera_")]
    
    @property
    def available_audio_backends(self) -> List[str]:
        """
        Retrieves a list of available audio backend configurations.

        :returns: Available audio backend configuration names.
        """
        return [n for n in self.list() if n.startswith("audio_")]
    
    @property
    def available_speech_backends(self) -> List[str]:
        """
        Retrieves a list of available speech backend configurations.

        :returns: Available speech backend configuration names.
        """
        return [n for n in self.list() if n.startswith("speech_")]

    @classmethod
    @lru_cache(maxsize=1)
    def get(cls) -> "ConfigManager":
        """
        Retrieves a singleton instance of the ConfigManager.

        :returns: A singleton instance of the class.
        """
        return ConfigManager()


config_manager = ConfigManager.get()
