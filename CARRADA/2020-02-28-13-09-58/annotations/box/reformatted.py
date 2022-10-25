import json

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
print(data[f"{all_keys[0]}"]["boxes"])  # <class 'list'>
print(data[f"{all_keys[0]}"]["labels"]) # <class 'list'>





# store an indentted version of the annotations as .txt file
def store():
    json_string = json.dumps(data, indent=4)
    # print(type(json_string)) # <class 'str'>
    # print(json_string)
    with open(CURR_PATH + "rd_formatted.txt", "w") as text_file:
        # write the whole string into a .txt file, it'll also store the indentation
        text_file.write(json_string)

