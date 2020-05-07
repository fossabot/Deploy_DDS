'''
This module is develope to test and verify accuracy of 
error based clustering model.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import random

#generating first data point in 2D
def mixed_datapoint_cluster(data_points,no_clusters):
    '''
    This method will generate cluster by mixing data points
    and return dataset generated based on that cluster 
    '''
    data = pd.DataFrame([],columns=['x','y'])


    #cluster-3
    data1 = pd.DataFrame([])
    x1 = np.linspace(30,50,data_points)
    delta1 = np.random.normal(0,0,x1.size)
    y1 = 60 +(-1/3) * x1 + delta1
    plt.plot(x1,y1-delta1) #actual fit
    plt.scatter(x1,y1)
    data1['x'] = x1
    data1['y'] = y1
    data = pd.concat([data,data1])

    #cluster-2
    data2 = pd.DataFrame([])
    x2 = np.linspace(60,80,data_points)
    delta2 = np.random.normal(0,0,x2.size)
    y2 = x2 * 3 + delta2
    plt.plot(x2,y2-delta2) #actual fit
    plt.scatter(x2,y2)
    data2['x'] = x2
    data2['y'] = y2
    data = pd.concat([data,data2])

    #cluster-3
    data3 = pd.DataFrame([])
    x3 = np.linspace(-20,0,data_points)
    delta3 = np.random.normal(0,0,x3.size)
    y3 = 50 +10 * x3 + delta3
    plt.plot(x3,y3-delta3) #actual fit
    plt.scatter(x3,y3)
    data3['x'] = x3
    data3['y'] = y3
    data = pd.concat([data,data3])

    #cluster-4
    data4 = pd.DataFrame([])
    x4 = np.linspace(0,20,data_points)
    delta4 = np.random.normal(0,0,x4.size)
    y4 = 200 - 10 * x4 + delta4
    plt.plot(x4,y4-delta4) #actual fit
    plt.scatter(x4,y4)
    data4['x'] = x4
    data4['y'] = y4
    data = pd.concat([data,data4])

    data, test = train_test_split(data, test_size=0.2)
    plt.xlabel('X variable')
    plt.ylabel('Y variable')
    plt.title('Plot of Data generated')
    plt.savefig('Dataset_plot.eps')
    plt.show()
    data.to_csv('dataset.csv',index=False)
    test.to_csv('testset.csv',index=False)

data_points = 50 #data points in each cluster
mixed_datapoint_cluster(data_points,1)
print('done')