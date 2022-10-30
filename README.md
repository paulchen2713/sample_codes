# samples
try to read out the data and labels from several datasets, currently working on [CARRADA Dataset](https://ieeexplore.ieee.org/abstract/document/9413181)

(手動) ```convert_label.py``` 使用方式，把 ```convert_label.py``` 放在 ```./box/``` 裡面並更改當前資料夾路徑 ```CURR_PATH```，例如 ```"D:/Datasets/CARRADA/2020-02-28-13-09-58/annotations/box/"``` 就是處理 ```2020-02-28-13-09-58``` 這個資料夾內的標記資料，接著創一個新資料夾取名 labels，然後就可以直接執行了。

(自動) ```convert_label.py``` 使用方式，從 ```validated_seqs.txt``` 把所有資料夾名稱都讀出來存進一個 ```list()``` 這裡是取作 ```dir_names```，然後執行迭代過每個資料夾即可。
```dir_names = ['2019-09-16-12-52-12', '2019-09-16-12-55-51', '2019-09-16-12-58-42', '2019-09-16-13-03-38', '2019-09-16-13-06-41', '2019-09-16-13-11-12', '2019-09-16-13-13-01', '2019-09-16-13-14-29', '2019-09-16-13-18-33', '2019-09-16-13-20-20', '2019-09-16-13-23-22', '2019-09-16-13-25-35', '2020-02-28-12-12-16', '2020-02-28-12-13-54', '2020-02-28-12-16-05', '2020-02-28-12-17-57', '2020-02-28-12-20-22', '2020-02-28-12-22-05', '2020-02-28-12-23-30', '2020-02-28-13-05-44', '2020-02-28-13-06-53', '2020-02-28-13-07-38', '2020-02-28-13-08-51', '2020-02-28-13-09-58', '2020-02-28-13-10-51', '2020-02-28-13-11-45', '2020-02-28-13-12-42', '2020-02-28-13-13-43', '2020-02-28-13-14-35', '2020-02-28-13-15-36']```

```num_of_labels = [286, 273, 304, 327, 218, 219, 150, 208, 152, 174, 174, 235, 442, 493, 656, 523, 350, 340, 304, 108, 129, 137, 171, 143, 104, 81, 149, 124, 121, 98]```

number of directorie: 30
total number of labels: 7193

