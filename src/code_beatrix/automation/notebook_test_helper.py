# -*- coding: utf-8 -*-
"""
@file
@brief Some automation helpers to test notebooks and check they are still working fine.
"""
import os
from pyquickhelper.loghelper import noLOG
from pyquickhelper.ipythonhelper import execute_notebook_list


def ls_notebooks(subfolder):
    """
    Returns the list of notebooks in a particular subfolder.

    @param      subfolder   subfolder (related to this module)
    @return                 list of files
    """
    this = os.path.abspath(os.path.dirname(__file__))
    docnote = os.path.join(
        this,
        "..",
        "..",
        "..",
        "_doc",
        "notebooks",
        subfolder)
    notes = [
        os.path.normpath(
            os.path.join(
                docnote,
                _)) for _ in os.listdir(docnote)]

    keepnote = []
    for note in notes:
        ext = os.path.splitext(note)[-1]
        if ext != ".ipynb":
            continue
        keepnote.append(note)
    return keepnote


def get_additional_paths():
    """
    Returns a list of paths to add before running the notebooks,
    paths to :epkg:`pyquickhelper`, ...

    @return             list of paths
    """
    import pyquickhelper
    import jyquickhelper
    import ensae_projects
    import pyensae
    addpath = [os.path.dirname(pyquickhelper.__file__),
               os.path.dirname(jyquickhelper.__file__),
               os.path.dirname(ensae_projects.__file__),
               os.path.dirname(pyensae.__file__),
               os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."),
               ]
    addpath = [os.path.normpath(os.path.join(_, "..")) for _ in addpath]
    return addpath


def clean_function_notebook(code):
    """
    Cleans cells when unittesting notebooks.

    @param      code        cell content
    @return                 modified code
    """
    code = code.replace(
        'run_cmd("exemple.xlsx"',
        'skip_run_cmd("exemple.xlsx"')

    skip = ["faire une chose avec la probabilité 0.7",
            "# déclenche une exception",
            "# pour lancer Excel",
            "for k in list_exercice_1 :",
            "return ....",
            "return [ .... ]",
            "def __init__(self, ...) :",
            "if random.random() <= 0.7 :",
            "dictionnaire_depart.items() [0]",
            "iterateur(0,10) [0]",
            "# ...... à remplir",
            'String.Join(",", a.Select(c=>c.ToString()).ToArray())',
            "# elle n'existe pas encore",
            "from ggplot import *",
            # ggplot calls method show and it opens window blocking the offline
            # execution
            ]
    rep = [("# ...", "pass # "),
           ("%timeit", "#%timeit"),
           ]
    spl = ["# ......",
           "# elle n'existe pas encore",
           ]

    for s in skip:
        if s in code:
            return ""

    for s in spl:
        if s in code:
            code = code.split(s)[0]

    for s in rep:
        code = code.replace(s[0], s[1])

    return code


def execute_notebooks(folder, notebooks, filter, clean_function=None,
                      fLOG=noLOG, deepfLOG=noLOG):
    """
    Executes a list of notebooks.

    @param      folder          folder
    @param      notebooks       list of notebooks
    @param      filter          function which validate the notebooks
    @param      clean_function  cleaning function to apply to the code before running it
    @param      fLOG            logging function
    @param      deepfLOG        logging function used to run the notebook
    @return                     dictionary { notebook_file: (isSuccess, outout) }

    The signature of function ``filter`` is::

        def filter( i, filename) : return True or False

    """

    def valid_cell(cell):
        if "%system" in cell:
            return False
        if "df.plot(...)" in cell:
            return False
        if 'df["difference"] = ...' in cell:
            return False
        return True

    addpaths = get_additional_paths()
    if filter:
        notebooks = [_ for i, _ in enumerate(notebooks) if filter(i, _)]
    if len(notebooks) == 0:
        raise ValueError("Empty list of notebooks.")
    return execute_notebook_list(
        folder, notebooks, fLOG=fLOG, valid=valid_cell, additional_path=addpaths,
        clean_function=clean_function)
