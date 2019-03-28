"""
@brief      test log(time=1s)
"""
import unittest
from code_beatrix.faq.faq_python import instruction_pass


class TestPass(unittest.TestCase):

    def test_pass(self):
        instruction_pass()


if __name__ == "__main__":
    unittest.main()
