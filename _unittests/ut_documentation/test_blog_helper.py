"""
@brief      test log(time=4s)
@author     Xavier Dupre
"""

import sys
import os
import unittest
from docutils.parsers.rst import directives

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

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.helpgen import BlogPost, BlogPostList, BlogPostDirective


class TestBlogHelper(unittest.TestCase):

    def test_post_parse(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        directives.register_directive("blogpost", BlogPostDirective)

        path = os.path.abspath(os.path.split(__file__)[0])
        file = os.path.join(path, "..", "..", "_doc", "sphinxdoc",
                            "source", "blog", "2015", "2015-04-04_tinkerlab.rst")
        p = BlogPost(file)
        fLOG(p.title)
        assert len(p.title) > 0
        assert p.date == "2015-04-04"
        assert isinstance(p.Fields, dict)

    def test_post_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        directives.register_directive("blogpost", BlogPostDirective)

        path = os.path.abspath(os.path.split(__file__)[0])
        fold = os.path.join(
            path, "..", "..", "_doc", "sphinxdoc", "source", "blog")
        assert os.path.exists(fold)
        out = get_temp_folder(__file__, "temp_post_list")
        p = BlogPostList(fold)
        cats = p.get_categories()
        fLOG(cats)
        months = p.get_months()
        fLOG(months)
        assert len(p) > 0
        assert len(cats) > 0
        assert len(months) > 0

        res = p.write_aggregated(out)
        assert len(res) >= 4
        for r in res:
            assert os.path.exists(r)


if __name__ == "__main__":
    unittest.main()
