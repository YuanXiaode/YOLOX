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
import random

from yolox.utils.lr_scheduler import *

# lr,
# min_lr_ratio,
# warmup_lr_start,
# total_iters,
# normal_iters,
# no_aug_iters,
# warmup_total_iters,
# semi_iters,
# iters_per_epoch,
# iters_per_epoch_semi,
# iters,



is_in_boxes = torch.ones((2,10))

is_in_boxes_anchor = torch.zeros((10))
is_in_boxes_anchor[0] = 1
is_in_boxes_anchor[1] = 1
is_in_boxes_anchor = is_in_boxes_anchor.bool()
print(is_in_boxes_anchor)


print(is_in_boxes[:, is_in_boxes_anchor])