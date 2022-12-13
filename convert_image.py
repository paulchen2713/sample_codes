# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:15:19 2022

@patch: 2022.10.31
@author: Paul
@file: convert_image.py
@dependencies:
    envs        pt3.7
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import time

# set the dataset path
DATASET = 'D:/Datasets/CARRADA/'
DATASET2 = 'D:/Datasets/CARRADA2/'

# directory names, number of directorie: 30
dir_names = ['2019-09-16-12-52-12', '2019-09-16-12-55-51', '2019-09-16-12-58-42', '2019-09-16-13-03-38', '2019-09-16-13-06-41', 
             '2019-09-16-13-11-12', '2019-09-16-13-13-01', '2019-09-16-13-14-29', '2019-09-16-13-18-33', '2019-09-16-13-20-20', 
             '2019-09-16-13-23-22', '2019-09-16-13-25-35', '2020-02-28-12-12-16', '2020-02-28-12-13-54', '2020-02-28-12-16-05', 
             '2020-02-28-12-17-57', '2020-02-28-12-20-22', '2020-02-28-12-22-05', '2020-02-28-12-23-30', '2020-02-28-13-05-44', 
             '2020-02-28-13-06-53', '2020-02-28-13-07-38', '2020-02-28-13-08-51', '2020-02-28-13-09-58', '2020-02-28-13-10-51', 
             '2020-02-28-13-11-45', '2020-02-28-13-12-42', '2020-02-28-13-13-43', '2020-02-28-13-14-35', '2020-02-28-13-15-36']

# number of images / labels in each directory, total number of labels: 7193
num_of_images = [286, 273, 304, 327, 218, 219, 150, 208, 152, 174, 
                 174, 235, 442, 493, 656, 523, 350, 340, 304, 108, 
                 129, 137, 171, 143, 104, 81, 149, 124, 121, 98]

# e.g. read "validated_seqs.txt"
def read_txt_file(file_name=""):
    dir_names = list()
    with open(DATASET + file_name, "r") as seqs_file:
        dir_names = seqs_file.read().splitlines()
    return dir_names
# temp = read_txt_file("validated_seqs.txt")


def main():
    for dir_name in dir_names: # [23:24]: # 
        # e.g. "D:/Datasets/CARRADA/2020-02-28-13-09-58/annotations/box/"
        print(f"current directory: {dir_name}")

        # set the file path
        seq_path = DATASET + dir_name + '/'
        print(f"current seq path: {seq_path}")

        # "range_doppler_light.json", "range_angle_light.json"
        file_index = ["range_doppler_light.json", "range_angle_light.json"]
        with open(DATASET + f"{dir_name}/annotations/box/" + f"{file_index[0]}", "r") as json_file:
            data = json.loads(json_file.read())
        # extract all keys from the dict, and store them in a list()
        all_keys = list(data.keys())

        for key in all_keys: # [62:63]: #
            print(f"frame name: \"{key}\"")

            # set matrix and image path
            rd_path = seq_path + 'range_doppler_numpy/' + key + '.npy'
            ra_path = seq_path + 'range_angle_numpy/' + key + '.npy'
            # img_path = seq_path + 'camera_images/' + key + '.jpg'

            # load the RDM, RAM
            rd_matrix = np.load(rd_path)
            ra_matrix = np.load(ra_path)
            # print(f"rd_matrix.shape = {rd_matrix.shape}") # (256, 64)
            # print(f"ra_matrix.shape = {ra_matrix.shape}") # (256, 256)

            seq_path2 = DATASET2 + "RD/" + dir_name + '/'
            store_path = seq_path2 + "images/"
            # print(f"store path: \"{store_path}\"") # e.g. "D:/Datasets/CARRADA/2020-02-28-13-09-58/RD_maps/images/""
            
            plt.matshow(rd_matrix, interpolation="nearest") # 310 x 1240
            # plt.imshow(
            #     rd_matrix, 
            #     # extent=[0, 1, 0, 1]
            # ) # 92 x 369
            plt.plasma()
            plt.axis('off')
            plt.savefig(store_path + f'{key}.png', bbox_inches='tight', pad_inches=0)

            # RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface 
            # (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. 
            # (To control this warning, see the rcParam `figure.max_open_warning`).
            
            plt.clf() # clears the entire current figure 
            plt.close(plt.gcf()) # ref. https://heitorpb.github.io/bla/2020/03/18/close-matplotlib-figures/

            # plt.show()



if __name__ == '__main__':
    tic = time.perf_counter()
    main()
    toc = time.perf_counter()
    duration = toc - tic
    print(f"duration: {duration:0.4f} seconds") 
    print(duration)
    # rd_matrix duration: 1280.4447068 seconds
    # ra_matrix duration: 871.3378964 seconds

