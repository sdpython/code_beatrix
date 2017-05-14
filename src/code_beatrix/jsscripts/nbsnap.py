"""
@file
@brief Snap rendering in a notebook.
"""
import uuid
import os
import glob
from .snap import __file__ as location_js_snap


class RenderSnapRaw(object):
    """
    Render `Snap <https://snap.berkeley.edu/>`_ using javascript.
    """

    def __init__(self, width="1000", height="600", divid=None, filename=None):
        """
        initialize

        @param  width           (str) width
        @param  height          (str) height
        @param  divid           (str|None) id of the div
        @param  filename        (str|None) filename
        """
        if divid == "scratch_div_id":
            # we should use a static counter but it
            # is very unlikely more than one snap will be added to
            # a notebook
            divid += "_%s" % str(uuid.uuid4()).replace("-", "")

        self.filename = filename
        self.divid = divid if divid else str(uuid.uuid4()).replace("-", "")
        self.width = width
        self.height = height

    def generate_html(self):
        """
        Return a couple (HTML, JS).
        """
        w = self.width
        h = self.height
        divid = self.divid

        js_path = os.path.dirname(location_js_snap)
        files = [os.path.split(_)[-1] for _ in glob.glob(js_path + "/*.js")]
        path = "/static/snap/"
        js_libs = [path + _ for _ in files]

        html_src = """
            <div id="__DIV__div" style="position:relative; width:__WIDTH__px; height:__HEIGHT__px;">
            Snap showing up soon...
            <canvas id="__DIV__" style="width:__WIDTH__px; height:__HEIGHT__px; position:relative; " />
            </div>
            """.replace("__DIV__", divid).replace("__WIDTH__", w).replace("__HEIGHT__", h)
        test_js = """<script>
                     var world__DIV__;
                     function loop__DIV__() {
                        world__DIV__.doOneCycle();
                     }
                     function start_snap__DIV__() {
                        var sec = document.getElementsByClassName("__DIV__div");
                        sec.innerHTML = "loading...";
                        world__DIV__ = new WorldMorph(document.getElementById('__DIV__'));
                        world__DIV__.worldCanvas.focus();
                        new IDE_Morph().openIn(world__DIV__);
                        setInterval(loop__DIV__, 1);
                        sec.innerHTML = "";
                     }
                     window.setTimeout(start_snap__DIV__,500);
                     </script>
                     """.replace("__DIV__", divid)
        libs = [
            '<script type="text/javascript" src="{0}"></script>'.format(l) for l in js_libs]
        libs = "\n".join(libs)

        return html_src, libs + "\n" + test_js


class RenderSnap(RenderSnapRaw):
    """
    Render Snap using javascript, outputs only HTML.
    """

    def _repr_html_(self):
        ht, js = self.generate_html()
        ht += "{0}".format(js)
        return ht
