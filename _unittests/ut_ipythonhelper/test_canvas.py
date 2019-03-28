# -*- coding: utf-8 -*-
"""
@brief      test log(time=3s)
"""
import unittest
from code_beatrix.ipythonhelper import display_canvas_point


class TestCanvas(unittest.TestCase):

    def test_canvas(self):
        points = display_canvas_point('gid')
        self.assertEqual(points, [])


if __name__ == "__main__":
    unittest.main()
