# -*- coding: utf-8 -*-
"""Softmax_Cross_Entropy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1epFnWJHDxYc6a26HExEwxOJvYoV00lov
"""

import torch

import torch.nn as nn

import numpy as np

def softmax(x):
  return np.exp(x) / np.sum(np.exp(x), axis = 0)

x = np.array([2.0, 1.0, 0.1])
outputs = softmax(x)
print('Softmax numpy: ', outputs)

x = torch.tensor([2.0, 1.0, 0.1])
outputs = torch.softmax(x, dim = 0)
print(outputs)
