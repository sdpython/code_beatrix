#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to handle files
"""
import os
import glob
from IPython.core.magic import magics_class, line_magic
from IPython.core.display import HTML, display_html, Javascript

from pyquickhelper import MagicCommandParser, MagicClassWithHelpers
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
        parser = MagicCommandParser(
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
            default="scratch-div-id",
            help='id for the HTML div')
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
            if args.f in [None, ""]:
                #filename = None
                pass
            else:
                raise NotImplementedError()

            iddiv = args.div

            js_path = os.path.dirname(location_js_snap)
            files = [os.path.split(_)[-1]
                     for _ in glob.glob(js_path + "/*.js")]
            path = "/static/snap/"
            js_libs = [path + _ for _ in files]

            html_src = """
                <div id="{0}"> </div>
                """.format(iddiv)
            test_js = """
                         var world;
                         window.onload = function () {
                            world = new WorldMorph(document.getElementById('{0}'));
                            world.worldCanvas.focus();
                            new IDE_Morph().openIn(world);
                            setInterval(loop, 1);
                         };
                         function loop() {
                            world.doOneCycle();
                         }
                         """.format(iddiv)
            display_html(HTML(data=html_src))
            return Javascript(data=test_js, lib=js_libs)


def register_scratch_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicScratch)
