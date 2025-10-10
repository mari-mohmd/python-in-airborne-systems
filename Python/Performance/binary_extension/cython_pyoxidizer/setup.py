# See Readme file
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("one_billion_loop.pyx")
)
