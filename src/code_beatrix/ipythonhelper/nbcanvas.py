"""
@file
@brief Drawing from a canvas
"""
import IPython
import IPython.core.display as ipydisplay
from IPython.display import display_html, display_javascript, Javascript, HTML
from .path_helper import local_d3js


def display_canvas_point(html_id, width=800, heigth=400, var_name="points"):
    """
    Adds a canvas to draw from a notebook, the code use javascript.

    @param      height      height
    @param      width       width
    @param      html_id     the function adds a div section, it should be different for every canevas
    @param      var_name    the function adds this variable to the kernel workspace

    @return                 the list of points
    """
    js_libs = local_d3js()

    # http://jsfiddle.net/yonester/9tr7w/2/
    html_src = """
    <div id="{0}"></div>
    """.format(html_id)

    points = []

    test_d3_js = """
    var r;

    var command0 ="__VARNAME__=[]";
    var kernel = IPython.notebook.kernel;
    kernel.execute(command0);

    var vis = d3.select("#__ID__").append("svg")
        .attr("width", __WIDTH__)
        .attr("height", __HEIGHT__)
        .style('border', '1px solid black')
        .on("mousedown", mousedown)
        ;

    function mousedown() {
        var m = d3.mouse(this);
        r = vis.append("rect")
            .attr("class", "myrect")
            .attr("style", "fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,255);")
            .attr("x", m[0])
            .attr("y", m[1])
            .attr("width", 5)
            .attr("height", 5);
        var command = "__VARNAME__.append( (" + m[0] + ", -" + m[1] + ") )";
        kernel.execute(command);
    }
    """ .replace("__WIDTH__", str(width)) \
        .replace("__HEIGHT__", str(heigth)) \
        .replace("__ID__", html_id)\
        .replace("__VARNAME__", var_name)
    js_libs = [js_libs]
    if 'display' not in dir(ipydisplay):
        # Weird bug introduced in IPython 8.0.0
        import IPython.core.display_functions
        ipydisplay.display = IPython.core.display_functions.display
    display_html(HTML(data=html_src))
    display_javascript(Javascript(data=test_d3_js, lib=js_libs))

    return points
