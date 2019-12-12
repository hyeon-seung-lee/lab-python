import os

import pandas as pd

"""
def change_label_to_int(self):
    if type(self.dataset.iloc[4]) == type(int):
        pass
    else:
        length = len(self.dataset)
        label = []
        for row in range(length):
            label.append(self.dataset.iloc[row, self.label_col_num])
        set_label = dict
        for index, label in enumerate(list(set(label))):
            set_label[label] = index
        temp_label = []
        for lb in label:
            for key, item in set_label.items():
                if lb == key:
                    temp_label.append(key)
                    break
                else:
                    continue
        print(temp_label)
"""
def change_label_to_int(self):
    if type(self.dataset.iloc[0,4]) == type(int()):
        pass
    else:
        length = len(self.dataset)
        label = []
        for row in range(length):
            label.append(self.dataset.iloc[row, 4])
        print(label)
        set_label = dict()
        for index, lbl in enumerate(list(set(label))):
            set_label[lbl] = index
        print(set_label)
        temp_label = []
        for lb in label:
            for key, item in set_label.items():
                if lb == key:
                    temp_label.append(item)

                else:
                    continue
        print(temp_label)
        temp_label=pd.DataFrame(temp_label)

        del self.dataset[4]
        print(self.dataset.head())
        result_df=pd.concat([self.dataset, temp_label],axis=1)
        result_df.columns=[0,1,2,3,'label']
        print(result_df.head())




#
# iris_file = os.path.join('..', 'scratch11', 'iris.csv')
# iris_dataset = pd.read_csv(iris_file, header=None)
# print(iris_dataset.head())
# change_label_to_int(iris_dataset)

dict = {'a': 1 , 'b' : 2 , 'c' : 3}
print(max(dict.values()))