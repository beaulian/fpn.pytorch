import os
import torch
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
#this_file = os.path.dirname(__file__)

sources = []
headers = []
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/nms_cuda.cpp', 'src/nms_cuda_kernel.cu']
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)

if with_cuda:
    setup(
        name='nms',
        ext_modules=[
            CUDAExtension(
                name='nms',
                sources=sources,
                include_dirs=['src'],
                extra_compile_args={'cxx': ['-g'],
                                    'nvcc': ['-O2']})
        ],
        cmdclass={
            'build_ext': BuildExtension
        }
    )

