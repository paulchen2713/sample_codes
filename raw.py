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

import numpy as np
import matplotlib.pyplot as plt

DATASET = 'D:/Datasets/CARRADA/Carrada/'

seq_name = '2020-02-28-13-09-58'
instances = ['001114', '001115']
frame_name = '000117'

seq_path = DATASET + seq_name + '/'
rd_path = seq_path + 'range_doppler_numpy/' + frame_name + '.npy'
ra_path = seq_path + 'range_angle_numpy/' + frame_name + '.npy'
img_path = seq_path + 'camera_images/' + frame_name + '.jpg'

ra_matrix = np.load(ra_path)
print(f"ra_matrix.shape = {ra_matrix.shape}")
rd_matrix = np.load(rd_path)
print(f"rd_matrix.shape = {rd_matrix.shape}")

print("rd_matrix: ")
print(rd_matrix)
print("ra_matrix: ")
print(ra_matrix)

# plt.plot(ra_matrix)
plt.plot(rd_matrix)
plt.show()

