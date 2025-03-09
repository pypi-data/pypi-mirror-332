# vim: set ts=4 sw=4 :
# _*_ coding: utf-8 _*_
# Copyright (c) 2025 TMQ Authors
# SPDX-License-Identifier: MPL-2.0

__author__ = 'Martin Wawro'

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension

setup(
    name="tmq",
    version="0.1.0",
    author="Martin Wawro",
    author_email="martin.wawro@gmail.com",
    package_dir={"" : "src"},
    description="Quantization aware machine learning",
    ext_modules=[
        CUDAExtension("tmq_cuda", [
            "src/tmq/tmq_cuda.cu"
        ]),
        CppExtension("tmq_native", [
            "src/tmq/tmq_native.cpp"
        ]),
    ],
    install_requires=[
        "torch>=2.1"
    ],
    cmdclass={ "build_ext" : BuildExtension},
    python_requires=">=3.8"
)
