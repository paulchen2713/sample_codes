# samples
try to read out the data and labels from several datasets, currently working on [CARRADA Dataset](https://ieeexplore.ieee.org/abstract/document/9413181)

(手動) ```convert_label.py``` 使用方式，把 ```convert_label.py``` 放在 ```./box/``` 裡面並更改當前資料夾路徑 ```CURR_PATH```，例如 ```"D:/Datasets/CARRADA/2020-02-28-13-09-58/annotations/box/"``` 就是處理 ```2020-02-28-13-09-58``` 這個資料夾內的標記資料，接著創一個新資料夾取名 labels，然後就可以直接執行了。
(自動) ```convert_label.py``` 使用方式，從 ```validated_seqs.txt``` 把所有資料夾名稱都讀出來存進一個 ```list()``` 這裡是取作 ```dir_names```，然後執行迭代過每個資料夾即可。
