from abc import ABC
from abc import abstractmethod

from typing import Dict
from typing import Any

class GripperBase(ABC):
    """
    A general class that models a gripper/hand
    """
    
    @abstractmethod
    def open(self) -> None:
        """
        Opens the gripper / hand
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Closes the gripper / hand
        """
        pass

    @abstractmethod
    def get_obs(self) -> Dict[str, Any]:
        """
        Gets the normalized position of the finger joints

        :returns: joint positions
        """
        pass

    @abstractmethod
    def is_open(self) -> bool:
        """
        Returns whether the hand/gripper is open

        :returns: True if the gripper is open
        """
        pass
    
    #@property
    ##abstractmethod
    #def gripper_name(self):
    #    pass