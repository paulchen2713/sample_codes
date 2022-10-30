# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:17:12 2022

@patch: 2022.10.30
@author: Paul
@file: convert_label.py
@dependencies:
    envs        pt3.7
"""

import json

def main():
    dir_names = list()
    with open("D:/Datasets/CARRADA/validated_seqs.txt", "r") as seqs_file:
        dir_names = seqs_file.read().splitlines()
        # print(dir_names)
        # print(type(dir_names))

    for dir_name in dir_names:
        # e.g. "D:/Datasets/CARRADA/2019-09-16-12-58-42/annotations/box/"
        print(f"current directory: {dir_name}")

        CURR_PATH = f"D:/Datasets/CARRADA/{dir_name}/annotations/box/"
        # "range_doppler_light.json", "range_angle_light.json"
        with open(CURR_PATH + "range_doppler_light.json", "r") as json_file:
            """
            # there are two ways to read json file
            # data = json.load(json_file)         # one using json.load(), which load the json_file
            # data = json.loads(json_file.read()) # make sure you add ".read()" when using json.loads(), the "s" means string
            """
            data = json.loads(json_file.read())
            # print(type(data)) # <class 'dict'>

        # extract all keys from the dict, and store them in a list()
        all_keys = list(data.keys())
        # print(data[f"{all_keys[0]}"]["boxes"])  # [[69, 32, 72, 35]] <class 'list'>
        # print(data[f"{all_keys[0]}"]["labels"]) # [1] <class 'list'>

        for key in all_keys:
            print(f"frame name: \"{key}\"")
            # print(f"everything: {data[key]}")
            # print(f"num of boxes: {len(data[key]['boxes'])}")
            # print(f"num of labels: {len(data[key]['labels'])}")

            if (len(data[key]['boxes']) != len(data[key]['labels'])): 
                print("boxes and labels are mismatched!")

            with open(CURR_PATH + f"labels/{key}.txt", "w") as label_txt_file:
                # in each rd_matrix / image it may contain 1~3 possible targets
                for index in range(0, len(data[key]['boxes'])):
                    # print(data[key]['boxes'][index])
                    # print(data[key]['labels'][index])

                    x, y, w, h = data[key]['boxes'][index][0:4]   # extract COCO format in absolute scale
                    x, y, w, h = x / 256, y / 64, w / 256, h / 64 # convert to YOLO format in relative scale
                    # print(f"x, y, w, h = {x}, {y}, {w}, {h}")
                    class_index = data[key]['labels'][index] - 1
                    # print(f"class_index = {class_index}")

                    print(f"{class_index} {x} {y} {w} {h}", file=label_txt_file) # redirect 'print()' output to a file

                    # print("---------------------------")


if __name__ == '__main__':
    main()


