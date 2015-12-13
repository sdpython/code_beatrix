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

    @todo Check about local d3.js
    """
    return default
    # return "/static/d3js/d3.v3.min.js"

    # the local version does not seem to work
    # to be checked later
    import ipython
    pyt = os.path.dirname(ipython.__file__)
    pack = os.path.join(pyt, "html")
    for f in ["/static/d3js/d3.min.js",
              "/static/d3js/d3.v3.min.js", ]:
        ff = os.path.join(pack, f)
        if os.path.exists(ff):
            return f
    return default
