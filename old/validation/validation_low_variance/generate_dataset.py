'''
This module is develope to test and verify accuracy of 
error based clustering model.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#generating first data point in 2D
def mixed_datapoint_cluster(data_points,no_clusters):
    '''
    This method will generate cluster by mixing data points
    and return dataset generated based on that cluster 
    '''
    data = pd.DataFrame([],columns=['x','y'])
    #cluster-1
    data1 = pd.DataFrame([])
    x1 = np.linspace(-20,20,data_points)
    delta1 = np.random.normal(0,1,x1.size)
    y1 = x1* 2+ delta1
    plt.plot(x1,y1-delta1) #actual fit
    plt.scatter(x1,y1)
    data1['x'] = x1
    data1['y'] = y1
    data = pd.concat([data,data1])

    # #cluster-1
    # data2 = pd.DataFrame([])
    # x2 = np.linspace(-20,20,data_points)
    # delta2 = np.random.normal(0,3,x2.size)
    # y2 = x2 * 9 + delta2
    # plt.plot(x2,y2-delta2) #actual fit
    # plt.scatter(x2,y2)
    # data2['x'] = x2
    # data2['y'] = y2
    # data = pd.concat([data,data2])

    # #cluster-1
    # data3 = pd.DataFrame([])
    # x3 = np.linspace(-20,20,data_points)
    # delta3 = np.random.normal(0,0.7,x3.size)
    # y3 = 0.5 - 3 * x3 + delta3
    # plt.plot(x3,y3-delta3) #actual fit
    # plt.scatter(x3,y3)
    # data3['x'] = x3
    # data3['y'] = y3
    # data = pd.concat([data,data3])
    plt.xlabel('X variable')
    plt.ylabel('Y variable')
    plt.title('Plot of Data generated')
    data.to_csv('dataset.csv',index=False)
    plt.savefig('Dataset_plot.eps')
    plt.show()

data_points = 500 #data points in each cluster
mixed_datapoint_cluster(data_points,1)
print('done')