"""
@file
@brief Copies files to the proper location.
"""

import os
from pyquickhelper.filehelper import synchronize_folder


def copy_jstool2notebook(tool, force=False):
    """
    Copies a tool to :epkg:`notebook` folder.

    @param      tool        tool name (snap for example)
    @param      force       do the copy even if the destination folder exists
    @return                 list of copied files
    """
    import notebook
    dest = os.path.join(os.path.dirname(notebook.__file__), "static")
    src = os.path.join(os.path.dirname(__file__), tool)
    if not os.path.exists(src):
        raise FileNotFoundError("unable to find tool: " + tool)
    dest = os.path.join(dest, tool)
    if not os.path.exists(dest):
        os.mkdir(dest)
        return synchronize_folder(src, dest)
    elif force:
        return synchronize_folder(src, dest)
    else:
        return None
