"""
@brief      test log(time=0s)
"""
import unittest
from code_beatrix import check


class TestCheckScratchFiles(unittest.TestCase):

    def test_check(self):
        check(kind="scratch")


if __name__ == "__main__":
    unittest.main()
