# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup
from pyquicksetup import read_version, read_readme, default_cmdclass


#########
# settings
#########

project_var_name = "code_beatrix"
project_owner = "sdpython"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = [project_var_name, 'Xavier Dupré', 'teaching', 'coding goûter',
            'kids']
DESCRIPTION = """Exercices pour apprendre la programmation, les algorithmes, et faire des coding goûters."""
CLASSIFIERS = [
    'Programming Language :: Python :: %d' % sys.version_info[0],
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".algorithm.data": ["*.txt"],
                project_var_name + ".scratchs.example_echiquier": ["*.sb2"],
                project_var_name + ".scratchs.example_tri": ["*.sb2"],
                project_var_name + ".scratchs.example_pyramide": ["*.sb2"],
                project_var_name + ".scratchs.example_chute": ["*.sb2"],
                project_var_name + ".jsscripts.snap": ["*.*"],
                project_var_name + ".jsscripts.snap.Backgrounds": ["*.*"],
                project_var_name + ".jsscripts.snap.Costumes": ["*.*"],
                project_var_name + ".jsscripts.snap.libraries": ["*.*"],
                project_var_name + ".jsscripts.snap.Sounds": ["*.*"],
                project_var_name + ".jsscripts.Snapin8r2": ["*.*"],
                project_var_name: ["rss_blog_list.xml"],
                }

setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name, subfolder='src'),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/code_beatrix/helpsphinx/",
    download_url="https://github.com/sdpython/code_beatrix/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=default_cmdclass(),
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=["pyquicksetup"],
    install_requires=["pyquickhelper>=1.10"],
    extras_require={
        'art': ['pytube3', 'moviepy==1.0.0'],
        'faq': ['pytube3'],
    }
)
