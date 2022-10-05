# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 19:34:27 2022

@patch: 2022.10.04
@author: Paul
@file: sample.py
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

import json
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# from carrada_dataset.utils.configurable import Configurable
from visualize_signal import SignalVisualizer
# from carrada_dataset.utils.transform_annotations import AnnotationTransformer
from generate_annotations import AnnotationGenerator
# from carrada_dataset.utils.transform_data import DataTransformer


# Sample to visualize
seq_name = '2020-02-28-13-09-58'
instances = ['001114', '001115']
frame_name = '000117'


# Define paths
DATASET = 'D:/Datasets/CARRADA/Carrada/'

seq_path = DATASET + seq_name + '/'
print(f"seq_path = {seq_path}") # seq_path = D:/Datasets/CARRADA/Carrada/2020-02-28-13-09-58/

rd_path = seq_path + 'range_doppler_numpy/' + frame_name + '.npy'
print(f"rd_path = {rd_path}") # rd_path = D:/Datasets/CARRADA/Carrada/2020-02-28-13-09-58/range_doppler_numpy/000117.npy

ra_path = seq_path + 'range_angle_numpy/' + frame_name + '.npy'
print(f"ra_path = {ra_path}") # ra_path = D:/Datasets/CARRADA/Carrada/2020-02-28-13-09-58/range_angle_numpy/000117.npy

img_path = seq_path + 'camera_images/' + frame_name + '.jpg'
print(f"img_path = {img_path}") # img_path = D:/Datasets/CARRADA/Carrada/2020-02-28-13-09-58/camera_images/000117.jpg

"""
# Path to the RAD tensor (soon available)
rad_path = os.path.join(seq_path, 'RAD_numpy', frame_name + '.npy')
"""

# annotations_path = os.path.join(DATASET, 'annotations_frame_oriented.json')
annotations_path = DATASET + 'annotations_frame_oriented.json'
print(f"annotations_path = {annotations_path}")

# Load data

# Annotations
with open(annotations_path, 'r') as fp:
    annotations = json.load(fp)
annotations = annotations[seq_name][frame_name]  # Keep annotations of interest
# print(f"annotations = {annotations}")


# Range-angle and range-Doppler matrices
"""
# the RA and RD matrices can be computed directly from the RAD tensor
rad_matrix = np.load(rad_path)
data_transformer = DataTransformer(rad_matrix)
ra_matrix = data_transformer.to_ra()
rd_matrix = data_transformer.to_rd()
"""
ra_matrix = np.load(ra_path)
print(f"ra_matrix.shape = {ra_matrix.shape}")
rd_matrix = np.load(rd_path)
print(f"rd_matrix.shape = {rd_matrix.shape}")


# Camera image of the scene
# print('Camera image of the scene {}, frame {}'.format(seq_name, frame_name))
print(f"Camera image of the scene {seq_name}, frame {frame_name}")
# Camera image of the scene 2020-02-28-13-09-58, frame 000117
img = Image.open(img_path)
# display(img)
plt.imshow(img)
plt.show()


# Range-Doppler visualization
signal_visualizer = SignalVisualizer(rd_matrix)
print('Raw Range-Doppler representation:')
signal_visualizer.save_scale(path='.', signal_type='range_doppler', color_scale=False, rotation=True, save_img=False, plot_img=True)

for annotation_type in ['sparse', 'dense', 'box']:
    for i, instance in enumerate(instances):
        points = annotations[instance]['range_doppler'][annotation_type]
        annot_generator = AnnotationGenerator(rd_matrix.shape, points)
        if annotation_type is 'sparse':
            annots = annot_generator.get_points()
        elif annotation_type is 'dense':
            annots = annot_generator.get_mask()
        else:
            annots = annot_generator.get_box()
        signal_visualizer.add_annotation(i, annots, annotation_type)
    print(f'Range-Doppler with {annotation_type} annotations:')
    signal_visualizer.save_multiple_annotations(path=f'/root/workspace/temp/rd_{annotation_type}.png',
                                                signal_type='range_doppler', color_scale=False,
                                                rotation=True, save_img=False, plot_img=True)
    signal_visualizer.reset_annotation()


# Range-Angle visualization
signal_visualizer = SignalVisualizer(ra_matrix)
print('Raw Range-Angle representation:')
signal_visualizer.save_scale(path='.', signal_type='range_angle', color_scale=False,
                             rotation=False, save_img=False, plot_img=True)
for annotation_type in ['sparse', 'dense', 'box']:
    for i, instance in enumerate(instances):
        points = annotations[instance]['range_angle'][annotation_type]
        annot_generator = AnnotationGenerator(ra_matrix.shape, points)
        if annotation_type is 'sparse':
            annots = annot_generator.get_points()
        elif annotation_type is 'dense':
            annots = annot_generator.get_mask()
        else:
            annots = annot_generator.get_box()
        signal_visualizer.add_annotation(i, annots, annotation_type)
    print('Range-Angle with {} annotations:'.format(annotation_type))
    signal_visualizer.save_multiple_annotations(path='/root/workspace/temp/ra_{}.png'.format(annotation_type),
                                                signal_type='range_angle', color_scale=False,
                                                rotation=False, save_img=False, plot_img=True)
    signal_visualizer.reset_annotation()


