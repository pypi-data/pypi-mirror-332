# Wavelet Neural Networks

[![PyPI - Version](https://img.shields.io/pypi/v/waveletnn?style=flat)](https://pypi.org/project/waveletnn/)
[![GitHub License](https://img.shields.io/github/license/Scurrra/WaveletNN-PyTorch?style=flat)](https://github.com/Scurrra/WaveletNN-PyTorch/tree/master?tab=MIT-1-ov-file)


Implementation of orthonormal and biorthogonal wavelet transforms via convolutions. Multibatch single-channel one- and -two-dimensional data is supported. For analysis kernels of even length are supported, while for inverse transform kernels are required to have length `4k + 2`. 

Package provides loss functions for wavelet's kernels regularizations to preserve features of both orthonormal and biorthogonal wavelets. 