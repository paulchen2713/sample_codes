# -*- coding: utf-8 -*-
"""
Created on Tue Oct 05 10:28:24 2022

@patch: 2022.10.05
@author: Paul
@file: raw.py
@dependencies:
    envs        test
    python      3.6.13
    ipython     7.16.1
    ipykernel   5.3.4
    numpy       1.19.5 (numpy-base 1.19.2)
    scipy       1.5.4
    torch       1.10.2
    torchvision 0.11.3
    matplotlib  3.3.4
"""

from operator import ge
import numpy as np
import matplotlib.pyplot as plt
import torchvision.transforms as T # for resizing the images
from PIL import Image              # for loading and saving the images

# set the dataset path
DATASET = 'D:/Datasets/CARRADA/Carrada/'

# set the file index
seq_name = '2020-02-28-13-09-58'
instances = ['001114', '001115']
frame_name = '000117'

# set the file path
seq_path = DATASET + seq_name + '/'
rd_path = seq_path + 'range_doppler_numpy/' + frame_name + '.npy'
ra_path = seq_path + 'range_angle_numpy/' + frame_name + '.npy'
img_path = seq_path + 'camera_images/' + frame_name + '.jpg'

# load the RDM, RAM
ra_matrix = np.load(ra_path)
print(f"ra_matrix.shape = {ra_matrix.shape}")
rd_matrix = np.load(rd_path)
print(f"rd_matrix.shape = {rd_matrix.shape}")

# print("rd_matrix: ")
# print(rd_matrix)
# print("ra_matrix: ")
# print(ra_matrix)

# a_file = open("test.txt", "a")
# for row in rd_matrix:
#     np.savetxt(a_file, row)
# a_file.close()

def get_shape(matrix):
    x, y = matrix.shape
    print(f"x, y = {x}, {y}")

get_shape(rd_matrix)
np.savetxt('D:/BeginnerPythonProjects/read_carrada/logs/000117_256_64.txt', rd_matrix, delimiter=' ')

plt.plasma()
plt.imshow(rd_matrix, extent=[0, 1, 0, 1])
# plt.xlim(-13.5, 13.5)
# plt.ylim(0, 50)
plt.savefig("D:/BeginnerPythonProjects/read_carrada/figs/000117_256_64.png")

# get_shape(ra_matrix)
# np.savetxt('D:/BeginnerPythonProjects/read_carrada/logs/000117_256_256.txt', ra_matrix, delimiter=' ')
# plt.imshow(ra_matrix, extent=[0, 1, 0, 1])
# plt.savefig("D:/BeginnerPythonProjects/read_carrada/figs/000117_256_256.png")

plt.show()

