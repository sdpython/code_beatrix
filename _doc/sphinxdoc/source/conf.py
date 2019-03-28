# -*- coding: utf-8 -*-
import sys
import os
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet
from code_beatrix import __version__ as sversion

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
import my_hachibee_sphinx_theme as hachibee_sphinx_theme


set_sphinx_variables(__file__, "Les enfants codaient", "Xavier Dupré", 2019,
                     "hachibee", hachibee_sphinx_theme.get_html_themes_path(),
                     locals(), add_extensions=['hachibee_sphinx_theme'],
                     custom_style='custom_style.css',
                     extlinks=dict(
                         issue=('https://github.com/sdpython/code_beatrix/issues/%s', 'issue')),
                     book=True, nblayout='table', doc_version=sversion)

html_show_copyright = False
html_title = "lesenfantcodaient.fr"
language = "fr"

blog_root = "http://lesenfantscodaient.fr/"

html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css', '_static/custom_style.css', '_static/style_notebook_snippet.css'],
}


custom_preamble = """\n
\\newcommand{\\vecteur}[2]{\\pa{#1,\\dots,#2}}
\\newcommand{\\N}[0]{\\mathbb{N}}
\\newcommand{\\indicatrice}[1]{\\mathbf{1\\!\\!1}_{\\acc{#1}}}
\\usepackage[all]{xy}
\\newcommand{\\infegal}[0]{\\leqslant}
\\newcommand{\\supegal}[0]{\\geqslant}
\\newcommand{\\ensemble}[2]{\\acc{#1,\\dots,#2}}
\\newcommand{\\fleche}[1]{\\overrightarrow{ #1 }}
\\newcommand{\\intervalle}[2]{\\left\\{#1,\\cdots,#2\\right\\}}
\\newcommand{\\loinormale}[2]{{\\cal N}\\pa{#1,#2}}
\\newcommand{\\independant}[0]{\\;\\makebox[3ex]{\\makebox[0ex]{\\rule[-0.2ex]{3ex}{.1ex}}\\!\\!\\!\\!\\makebox[.5ex][l]{\\rule[-.2ex]{.1ex}{2ex}}\\makebox[.5ex][l]{\\rule[-.2ex]{.1ex}{2ex}}} \\,\\,}
\\newcommand{\\esp}{\\mathbb{E}}
\\newcommand{\\var}{\\mathbb{V}}
\\newcommand{\\pr}[1]{\\mathbb{P}\\pa{#1}}
\\newcommand{\\loi}[0]{{\\cal L}}
\\newcommand{\\vecteurno}[2]{#1,\\dots,#2}
\\newcommand{\\norm}[1]{\\left\\Vert#1\\right\\Vert}
\\newcommand{\\dans}[0]{\\rightarrow}
\\newcommand{\\partialfrac}[2]{\\frac{\\partial #1}{\\partial #2}}
\\newcommand{\\partialdfrac}[2]{\\dfrac{\\partial #1}{\\partial #2}}
\\newcommand{\\loimultinomiale}[1]{{\\cal M}\\pa{#1}}
\\newcommand{\\trace}[1]{tr\\pa{#1}}
\\newcommand{\\abs}[1]{\\left|#1\\right|}
\\usepackage{movie15}
"""
# \\usepackage{eepic}

imgmath_latex_preamble += custom_preamble
latex_elements['preamble'] += custom_preamble
mathdef_link_only = True
html_split_index = True

epkg_dictionary['AudioClip'] = 'https://zulko.github.io/moviepy/ref/AudioClip/AudioClip.html'
epkg_dictionary['AudioArrayClip'] = 'https://zulko.github.io/moviepy/ref/AudioClip/AudioClip.html'
epkg_dictionary['deep learning'] = 'https://en.wikipedia.org/wiki/Deep_learning'
epkg_dictionary['fcn'] = 'https://github.com/wkentaro/fcn'
epkg_dictionary['gif'] = 'https://fr.wikipedia.org/wiki/Graphics_Interchange_Format'
epkg_dictionary['ImageClip'] = 'https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=imageclip#imageclip'
epkg_dictionary[
    'Mary Poppins'] = 'https://fr.wikipedia.org/wiki/Mary_Poppins_(film,_1964)'
epkg_dictionary['moviepy'] = 'https://zulko.github.io/moviepy/'
epkg_dictionary['opencv'] = 'https://opencv.org/'
epkg_dictionary['OpenShot'] = 'https://www.openshot.org/'
epkg_dictionary['pytube'] = 'https://github.com/nficano/pytube'
epkg_dictionary['SciTe'] = 'http://www.scintilla.org/SciTE.html'
epkg_dictionary['scratch'] = "https://scratch.mit.edu/"
epkg_dictionary['Scratch'] = 'https://scratch.mit.edu/'
epkg_dictionary['ShotCut'] = 'https://www.shotcut.org/'
epkg_dictionary['VideoClip'] = 'https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html'
epkg_dictionary['VLC'] = 'https://www.videolan.org/vlc/index.html'
epkg_dictionary['YouTube'] = "https://www.youtube.com/"
epkg_dictionary['youtube'] = "https://www.youtube.com/"
epkg_dictionary['wav'] = "https://fr.wikipedia.org/wiki/Waveform_Audio_File_Format"
