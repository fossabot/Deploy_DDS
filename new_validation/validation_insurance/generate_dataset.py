'''
This module is develope to test and verify accuracy of 
error based clustering model.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.model_selection import train_test_split

#generating first data point in 2D
data = pd.read_csv('auto-insurance.csv')
data, test = train_test_split(data, test_size=0.2)
plt.scatter(data['x'],data['y'])
plt.xlabel('X variable')
plt.ylabel('Y variable')
plt.title('Plot of Data generated')
plt.savefig('Dataset_plot.eps')
plt.show()
data.to_csv('dataset.csv',index=False)
test.to_csv('testset.csv',index=False)
