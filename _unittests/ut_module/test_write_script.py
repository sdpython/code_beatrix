"""
@brief      test tree node (time=5s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.pycode.setup_helper import write_module_scripts


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

from src.code_beatrix import __blog__


class TestWriteScript(unittest.TestCase):

    def test_write_script(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "appveyor":
            # does not work on appveyor
            return

        temp = get_temp_folder(__file__, "temp_write_script")

        res = write_module_scripts(temp, "win32", __blog__)
        self.assertTrue(len(res) > 1)
        for c in res:
            self.assertTrue(os.path.exists(c))
            with open(c, "r") as f:
                content = f.read()
            if "__" in content:
                for line in content.split("\n"):
                    if "__" in line and "sys.path.append" not in line and "__file__" not in line:
                        raise Exception(content)
            if ".xml" in c:
                if '<outline text="' not in content:
                    raise Exception(content)


if __name__ == "__main__":
    unittest.main()
