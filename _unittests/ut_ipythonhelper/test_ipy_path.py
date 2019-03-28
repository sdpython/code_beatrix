# -*- coding: utf-8 -*-
"""
@brief      test log(time=3s)
"""
import os
import unittest
from code_beatrix.ipythonhelper import local_d3js


class TestIpyPath(unittest.TestCase):

    def test_local_d3js(self):
        r = local_d3js()
        if "http://" not in r:
            assert os.path.exists(r)


if __name__ == "__main__":
    unittest.main()
