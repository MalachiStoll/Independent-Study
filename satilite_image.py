%matplotlib inline
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt 

import scipy.misc
scipy.misc.imread

from skimage import data

import zipfile

file = zipfile.ZipFile('Week-3-Numpy.zip', 'r')
data = file.read('wifire/sd-3layers.jpg')
data = imread('wifire/sd-3layers.jpg')