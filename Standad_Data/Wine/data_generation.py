import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# load dataset
data = pd.read_csv('winequality_white.csv')


data, test = train_test_split(data, test_size=0.1)
data.to_csv('dataset.csv',index=False)
test.to_csv('testset.csv',index=False)

