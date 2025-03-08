import time
import json
import numpy as np

class NumpyJSONEncoder(json.JSONEncoder):
    """Special json encoder for numpy types. Converts numpy array to a list."""

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        #elif isinstance(obj, np.bool):
        #    return super().default(obj)
        return json.JSONEncoder.default(self, obj)



class FrequencyTimer:
    """ keeps a loop frequency """

    def __init__(self, frequency):
        self.frequency = frequency
        self.period = 1.0 / frequency
        self.last_cycle = None

    def reset(self):
        """
        Resests the last cycle
        """
        self.last_cycle = time.monotonic()

    def wait_for_cycle(self):
        """
        Waits for the remaining period time. 
        First  cycle is skipped if ..func::reset hasn't been called.
        """
        if not self.last_cycle:
            self.last_cycle = time.monotonic()
            return

        elapsed_time = (time.monotonic() - self.last_cycle)
        time_remaining = self.period - elapsed_time

        if time_remaining > 0.001:
            time.sleep(time_remaining)
        self.last_cycle = time.monotonic()
