"""
@file
@brief Copy files to the proper location
"""

import os
from pyquickhelper import synchronize_folder


def copy_jstool2ipython(tool):
    """
    copy a tool to ipython folder

    @param      tool        tool name (snap for example)
    @return                 list of copied files
    """
    import IPython
    dest = os.path.join(os.path.dirname(IPython.__file__), "html", "static")
    src = os.path.join(os.path.dirname(__file__), tool)
    if not os.path.exists(src):
        raise FileNotFoundError("unable to find tool: " + tool)
    dest = os.path.join(dest, tool)
    if not os.path.exists(dest):
        os.mkdir(dest)
    return synchronize_folder(src, dest)
