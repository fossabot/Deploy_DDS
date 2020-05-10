import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd


# ##########################################
# #### for c9 and  C16 scheme
# data = pd.read_csv('dataset.csv')
# train,test = train_test_split(data,test_size=0.1)
# train.to_csv('train.csv',index=False)


# other_fuel = pd.read_csv('other_fuel.csv')
# test = pd.concat([test,other_fuel])
# test.to_csv('test.csv',index=False)

## for normal 
data = pd.read_csv('Alkane_Dataset_full_without_propane.csv')
train,test = train_test_split(data,test_size=0.1)
train.to_csv('train.csv',index=False)
test.to_csv('test.csv',index=False)