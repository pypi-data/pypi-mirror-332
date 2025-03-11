from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs = [np.get_include(), '../common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='pycocotools_holi',
    packages=['pycocotools_holi'],
    package_dir = {'pycocotools_holi': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython<=0.29.36',
        'matplotlib>=2.1.0'
    ],
    version='2.1',
    ext_modules= ext_modules
)
