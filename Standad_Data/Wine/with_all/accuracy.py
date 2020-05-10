import numpy as np
import pandas as pd
import os

path = './0.1/external_test_result/Ignition_delay_comparison/'
files = os.listdir(path=path)
print('files: ', files)

data = pd.DataFrame([])
for i in files:
    data_ = pd.read_csv(path+str(i))
    data = pd.concat([data_,data])

data['y_predicted'] = data['y_predicted'].round(0) 
print(data)
print('data_: ', data_)
from sklearn.metrics import accuracy_score

score = accuracy_score(data['y_predicted'], data['y_actual'])
print('score: ', score)

score = accuracy_score(data['y_predicted'], data['y_actual'], normalize=False)
print('score: ', score)

from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(data['y_actual'], data['y_predicted'])
print('matrix: ', matrix)

