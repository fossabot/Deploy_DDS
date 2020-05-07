import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('dataset.csv')
train,test = train_test_split(data,test_size=0.1)
train.to_csv('train.csv')


other_fuel = pd.read_csv('other_fuel.csv')
test = pd.concat([test,other_fuel])
test.to_csv('test.csv')