# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:56:29 2022

@patch: 2022.10.25
@author: Paul
@file: reformatted.py
@dependencies:
    envs        pt3.7
"""
import json

def main():
    CURR_PATH = "D:/Datasets/CARRADA/2020-02-28-13-09-58/annotations/box/"
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
    # print(data[f"{all_keys[28]}"]["boxes"])
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
            # one_line = str(data[key]['labels'][0]) 
            # label_txt_file.write(one_line)

            for index in range(0, len(data[key]['boxes'])):
                # print(data[key]['boxes'][index])
                # print(data[key]['labels'][index])

                x, y, w, h = data[key]['boxes'][index][0:4]   # extract COCO format in absolute scale
                x, y, w, h = x / 256, y / 64, w / 256, h / 64 # convert to YOLO format in relative scale
                # print(f"x, y, w, h = {x}, {y}, {w}, {h}")
                class_index = data[key]['labels'][index] - 1
                # print(f"class_index = {class_index}")

                print(f"{class_index} {x} {y} {w} {h}", file=label_txt_file)

                # print("---------------------------")


    # store an indentted version of the annotations as .txt file
    def store():
        json_string = json.dumps(data, indent=4)
        # print(type(json_string)) # <class 'str'>
        # print(json_string)
        with open(CURR_PATH + "rd_formatted.txt", "w") as text_file:
            # write the whole string into a .txt file, it'll also store the indentation
            text_file.write(json_string)
    # store()


if __name__ == '__main__':
    main()




