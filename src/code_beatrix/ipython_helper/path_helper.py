"""
@file
@brief Helpers around paths
"""

import os

#: default value for d3js
default_d3js = "http://rawgithub.com/mbostock/d3/master/d3.min.js"


def local_d3js(default=default_d3js):
    """
    try to find a local copy of d3js

    @param      default     use this value otherwise
    @return                 location of d3.min.js
    """
    return default

    # the local version does not seem to work
    # to be checked later
    user = os.environ["HOMEPATH"]
    join = os.path.join(user, ".ipython", "nbextensions")
    for f in ["d3.v3.min.js", "d3.min.js"]:
        ff = os.path.join(join, f)
        if os.path.exists(ff):
            return ff
    return default
