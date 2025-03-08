from dataclasses import dataclass
from dataclasses import field

import logging
import threading

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class ControlTypes:
    """
    Class representing different types of control methods.
    """
    position = "position"
    cartesian = "cartesian"
    motion_planning = "motion_planning"

control_types = ControlTypes()

class ControllerBase:
    """
    Base class for control methods.
    """

    def __init__(self, controller_type):
        """
        Initialize the controller.

        :param controller_type: Type of the controller.
        """
        self.controller_type = controller_type
        self.asynchronous = False

    @property
    def controller_name(self):
        return self.controller_type
    
    def set_asynchronous(self):
        """
        Set the controller to asynchronous mode.
        """
        self.asynchronous = True

    def set_synchronous(self):
        """
        Set the controller to synchronous mode.
        """
        self.asynchronous = False

    def start_controller(self):
        """
        Start the controller.
        """
        logger.info("starting controller %s", self.controller_name)

    def stop_controller(self):
        """
        Stop the controller.
        """
        logger.info("stopping controller %s", self.controller_name)

    def __enter__(self):
        """
        Start the controller when entering a context.

        :return: Self instance.
        """
        self.start_controller()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stop the controller when exiting a context.

        :param exc_type: Exception type.
        :param exc_value: Exception value.
        :param traceback: Traceback information.
        """
        self.stop_controller()

class ControlManager:
    """
    Manages multiple controllers and monitors their activation. 
    Only one controller should be active at the same time
    """

    def __init__(self):
        """
        Initialize the control manager.
        """
        self.controllers = {}
        self.active_controllers = []

    def register_controller(self, controller):
        """
        Register a controller.

        :param controller: Controller instance to register.
        """
        controller_name = controller.controller_name
        if controller_name in self.controllers:
            raise ValueError("Controller already registered.")

        self.controllers[controller_name] = controller

    def has_active_controllers(self) -> bool:
        """
        Check if there are active controllers.

        :return: True if active controllers exist, False otherwise.
        """
        return bool(self.active_controllers)

    def stop(self):
        """
        Stop all active controllers.
        """
        if not self.active_controllers:
            logger.info("No controller currently selected.")
            return

        self.active_controllers[0].stop()
        self.active_controllers.clear()

    def __call__(self, controller_name: str):
        """
        Activate a controller by name.

        :param controller_name: Name of the controller to activate.
        :return: Self instance if successful, None otherwise.
        """
        if controller_name not in self.controllers:
            raise ValueError("invalid controller name")

        if self.has_active_controllers():
            logger.error("Robot is currently controlled. Please disable controllers.")
            return None

        controller = self.controllers[controller_name]
        self.active_controllers.append(controller)

        return self

    def __enter__(self):
        """
        Enter the control manager's context.

        :return: Active controller instance.
        """
        if not self.active_controllers:
            logger.error("No controller currently selected.")
            return
        return self.active_controllers[0].__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the control manager's context, stopping controllers.

        :param exc_type: Exception type.
        :param exc_value: Exception value.
        :param traceback: Traceback information.
        """
        if not self.active_controllers:
            logger.error("No controller currently selected.")
            return
        try:
            self.active_controllers[0].__exit__(exc_type, exc_value, traceback)
        except Exception as e:
            logger.error("Unable to stop controllers! Exception was: %s", e)
            raise e
        finally:
            self.active_controllers.clear()

class BimanualControlManager(ControlManager):
    """
    Manages two control managers for bimanual control.
    """

    def __init__(self, control_right: ControlManager, control_left: ControlManager):
        """
        Initialize the bimanual control manager.

        :param control_right: Control manager for the right side.
        :param control_left: Control manager for the left side.
        """
        super().__init__()
        self.control_right = control_right
        self.control_left = control_left

    def move_home(self):            
        """
        """
        # Create threads
        right_thread = threading.Thread(target=self.control_right.move_home)
        left_thread = threading.Thread(target=self.control_left.move_home)

        # Start threads
        right_thread.start()
        left_thread.start()

        # Wait for both threads to finish
        right_thread.join()
        left_thread.join()

    