# Always prefer setuptools over distutils
#from distutils.core import setup
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import os

def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )

def find_packages(path, base="" ):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package( dir ):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

here = path.abspath(path.dirname(__file__))



# Get the long description from the README file
#with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()

setup(name='jeopardy_quiz',
      version='17.3.31.11am',
      description='A python tkinter script for learning about prograssive civil rights activism',
      #long_description=long_description,
      py_modules=['jeopardy_quiz'],
	  # Author Details
      author='Chelsea School Students',
      author_email='rgoldman@chelseaschool.edu',
      # homepage
      url='https://blog.9while9.com',
      # license
      license='GPLv2',
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Programming Language :: Python :: 2.7',
        'Topic :: Education',
        'Topic :: Sociology :: History',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft',
        'Intended Audience :: End Users/Desktop',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
    ],
      keywords='tkinter trivia learning game',
      packages=find_packages('.'),
      #install_requires=['webbrowser'],
      package_dir={
        'jeopardy_quiz': 'jeopardy_quiz'
        },
      entry_points={
        #'console_scripts': [
        #    'jeopardy_quiz = jeopardy_quiz.__main__:main'
        #    ],
        'gui_scripts': [
            'jeopardy_quiz = jeopardy_quiz.jeopardy_quiz:main',
            ]
        },




      )
