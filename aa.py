# encoding: utf-8
"""
      author: YuanXiaode
      file: aa
      time: 2021/8/31 13:50
"""
import setuptools
import re
import setuptools
import glob
from os import path
import torch
import os
from pathlib import Path
import yolox
import ast
import inspect
import cv2 as cv
import matplotlib.pyplot as plt
from pprint import pprint
import numpy as np

labels_t = np.ones((3,3))
labels_t = np.expand_dims(labels_t, 1)
print(labels_t.shape)