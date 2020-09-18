"""
TestVector - test for class Vector implementation
"""
import unittest
from random import randint
from collections import namedtuple

from vector import *


class TestVector(unittest.TestCase):

    """
    test_solve()
    """
    def test_solve(self):
        """
         test 100 equations and compare results with numpy solve method
        """
        li = []
        Para = namedtuple('Para', 'matrix vector')
        for i in range(100):
            rand = randint(2, 4)
            matrix = Vector(*[Vector(*[randint(-50, 50) for _ in range(rand)]) for _ in range(rand)])
            vector = Vector(*[randint(-50, 50) for _ in range(rand)])
            li.append(Para(matrix, vector))
        for elem in li:
            with self.subTest():
                np.testing.assert_equal(elem.vector.solve(elem.matrix).arr,
                                        np.linalg.solve(np.array([v.arr for v in elem.matrix.arr]), elem.vector.arr))


if __name__ == '__main__':
    unittest.main()
