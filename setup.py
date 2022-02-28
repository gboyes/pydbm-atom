import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


setup(
    name="pydbm-atom",
    version="0.1.0",
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("atom", ["atom.pyx"],
    include_dirs = [numpy.get_include()])],
    install_requires=["numpy"]
)
