import unittest

import time

from robits.core.utils import FrequencyTimer


class FrequencyTimerTest(unittest.TestCase):

    def test_period(self):
        timer = FrequencyTimer(1)
        self.assertEqual(1, timer.period)

        timer = FrequencyTimer(10)
        self.assertEqual(0.1, timer.period)

        timer = FrequencyTimer(30)
        self.assertEqual(1/30.0, timer.period)


    def test_cycle(self):
        timer = FrequencyTimer(100)
        timer.reset()
        start_time = time.time()
        for i in range(10):
            timer.wait_for_cycle()
        elapsed_time = time.time() - start_time

        self.assertLess(0.099, elapsed_time)
        self.assertLess(elapsed_time, 0.115)
