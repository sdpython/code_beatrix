"""
@brief      test tree node (time=5s)
"""
import os
import unittest
from pyquickhelper.pycode import get_temp_folder, skipif_appveyor
from pyquickhelper.pycode.setup_helper import write_module_scripts
from code_beatrix import __blog__


class TestWriteScript(unittest.TestCase):

    @skipif_appveyor("does not work on appveyor")
    def test_write_script(self):
        temp = get_temp_folder(__file__, "temp_write_script")

        res = write_module_scripts(temp, "win32", __blog__)
        self.assertTrue(len(res) > 1)
        for c in res:
            self.assertTrue(os.path.exists(c))
            with open(c, "r", encoding="ascii") as f:
                content = f.read()
            if "__" in content:
                for line in content.split("\n"):
                    if "__" in line and "sys.path.append" not in line and "__file__" not in line:
                        raise AssertionError(content)
            if ".xml" in c:
                if '<outline text="' not in content:
                    raise AssertionError(content)


if __name__ == "__main__":
    unittest.main()
