import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# load dataset
data = pd.read_csv('abalone.csv')

#label
number = LabelEncoder()
data['sex'] = number.fit_transform(data['sex'].astype(str))
print('data: ', data)

#one-hot encoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)

x = ct.fit_transform(data)
print('x: ', x)
columns = ['female','infant','male'] 
for i in range(1,len(list(data.columns))):
    columns.append(list(data.columns)[i])
print('columns: ', columns)
data = pd.DataFrame(x,columns =  columns)
print('data: ', data)


data, test = train_test_split(data, test_size=0.2)
data.to_csv('dataset.csv',index=False)
test.to_csv('testset.csv',index=False)

