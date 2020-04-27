import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold


# data sample
data = pd.read_csv('train.csv')
print('data: ', data)
# prepare cross validation
kf = KFold(3, shuffle = True)
print('kf: ', kf)
kf.get_n_splits(data)
# enumerate splits
index = 1
for train_index, test_index in kf.split(data):
	train_data , test_data = data.loc[train_index,:], data.loc[test_index,:]
	train_data.to_csv('train_'+str(index)+'.csv')
	test_data.to_csv('test_'+str(index)+'.csv')
	index += 1 