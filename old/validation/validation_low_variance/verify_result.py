import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import os
import subprocess 
import pathlib
import random

#reading dataset 
color = "#%06x" % random.randint(0, 0xFFFFFF)
# plt.scatter(data['x'],data['y_act'],marker='o',c=colour[i])
data_original = pd.read_csv("dataset.csv")
plt.scatter(data_original['x'],data_original['y'],label='No of Points:'+str(len(data_original)),marker='.',c=color)

def find_dir_n_files(dir_):
    print('dir_: ', dir_)
    file_list=os.listdir(str(dir_))
    print('file_list: ', file_list)
    return file_list


dir_ = './result/final_cluster'
dir_list = find_dir_n_files(dir_)
files_ = []
for j in dir_list:
    files_ = find_dir_n_files(str(dir_)+'/'+str(j))
    for i in range(len(files_)):
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        path_ = str(dir_)+'/'+str(j)+'/'+str(files_[i] )
        data = pd.read_csv(path_)
        cluster_label = files_[i].split('_')[-2]
        print('cluster_label: ', cluster_label)
        plt.scatter(data['x'],data['y_pred'],label='No of data:'+str(len(data))+' cluster: '+str(cluster_label) ,marker='x',c=color)
        plt.xlabel('X variable')
        plt.ylabel('Y variable')
        plt.legend()
plt.savefig('comparision_plot.eps')
plt.show()


