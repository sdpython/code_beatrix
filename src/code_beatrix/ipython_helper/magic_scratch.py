#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to handle files
"""
import os
import glob
import random
from IPython.core.magic import magics_class, line_magic
from IPython.core.display import HTML
from pyquickhelper.ipythonhelper import MagicCommandParser, MagicClassWithHelpers
from ..jsscripts.snap import __file__ as location_js_snap


@magics_class
class MagicScratch(MagicClassWithHelpers):

    """
    Defines magic commands to list the content of a folder

    .. versionadded:: 1.1
    """

    @staticmethod
    def snap_parser():
        """
        defines the way to parse the magic command ``%snap``
        """
        parser = MagicCommandParser(prog="snap",
                                    description='insert a snap window inside a notebook')
        parser.add_argument(
            '-f',
            '--file',
            type=str,
            default="",
            help='scratch or snap file to display')
        parser.add_argument(
            '-d',
            '--div',
            type=str,
            default="scratch_div_id",
            help='id for the HTML div')
        parser.add_argument(
            '-W',
            '--width',
            type=int,
            default=1000,
            help='window width')
        parser.add_argument(
            '-H',
            '--height',
            type=int,
            default=600,
            help='window height')
        return parser

    @line_magic
    def snap(self, line):
        """
        defines ``%snap``
        which inserts a snap window inside a notebook
        """
        parser = self.get_parser(MagicScratch.snap_parser, "snap")
        args = self.get_args(line, parser)

        if args is not None:
            if args.file in [None, ""]:
                #filename = None
                pass
            else:
                raise NotImplementedError()

            iddiv = args.div
            h = str(args.height)
            w = str(args.width)
            if iddiv == "scratch_div_id":
                # we should use a static counter but it
                # is very unlikely more than one snap will be added to
                # a notebook
                iddiv += "_%d" % random.randint(0, 100000)

            js_path = os.path.dirname(location_js_snap)
            files = [os.path.split(_)[-1]
                     for _ in glob.glob(js_path + "/*.js")]
            path = "/static/snap/"
            js_libs = [path + _ for _ in files]

            html_src = """
                <div id="__DIV__div" style="position:relative; width:__WIDTH__px; height:__HEIGHT__px;">
                Snap showing up soon...
                <canvas id="__DIV__" style="width:__WIDTH__px; height:__HEIGHT__px; position:relative; " />
                </div>
                """.replace("__DIV__", iddiv).replace("__WIDTH__", w).replace("__HEIGHT__", h)
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
                         """.replace("__DIV__", iddiv)
            libs = [
                '<script type="text/javascript" src="{0}"></script>'.format(l) for l in js_libs]
            libs = "\n".join(libs)
            return HTML(libs + "\n" + test_js + "\n" + html_src + "\n")


def register_scratch_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicScratch)
