import unittest

import numpy as np

from robits.core.data_model.action import CartesianAction

class ActionTest(unittest.TestCase):



    def test_rot_matrix(self):
        action = CartesianAction(position=np.zeros(3), quaternion=np.array([0, 0, 0, 1]), hand_open=False)
        expected = np.identity(3)
        self.assertTrue(np.allclose(expected, action.rot_matrix))



    def test_to_matrix(self):
        action = CartesianAction(position=np.zeros(3), quaternion=np.array([0, 0, 0, 1]), hand_open=False)
        expected = np.identity(4)
        actual = action.to_matrix()
        self.assertTrue(np.allclose(expected, actual))


    def test_from_matrix(self):
        action = CartesianAction.from_matrix(np.identity(4))

        expected_position = np.zeros(3)
        self.assertTrue(np.allclose(expected_position, action.position))


        expected_quaternion = np.array([0, 0, 0, 1])
        self.assertTrue(np.allclose(expected_quaternion, action.quaternion))

