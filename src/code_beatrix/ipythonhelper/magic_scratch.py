#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to handle files
"""
from IPython.core.magic import magics_class, line_magic
from pyquickhelper.ipythonhelper import MagicCommandParser, MagicClassWithHelpers
from ..jsscripts.nbsnap import RenderSnap


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
            return RenderSnap(h, w, iddiv)


def register_scratch_magics(ip):
    """
    register magics function, can be called from a notebook

    @param      ip      ip
    """
    ip.register_magics(MagicScratch)
