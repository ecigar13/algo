#!/usr/bin/venv python

from collections import defaultdict, Counter, deque
from heapq import *
import unittest
from typing import *
import sys
import os
import math
from parameterized import parameterized, parameterized_class

os.system('clear')


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction:() = (0,1)
        startx, starty = 0,0

        for instruction in instructions:
            if instruction == 'G':
                startx = startx + direction[0]
                starty = starty + direction[1]
            elif instruction == 'L':
                direction = (-direction[1], direction[0])
            else:
                direction = (direction[1], -direction[0])

        return (startx == 0 and starty == 0) or (direction != (0,1))

class TestMethods(unittest.TestCase):
    @parameterized.expand([
        ("14-3/2", 13),
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5), ("100000", 100000)
    ])
    def testEqual(self, numCourses: int, output):
        self.assertEqual(Solution().calculate(numCourses), output)


def print2d(matrix: [[]]):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    unittest.main(verbosity=0)
