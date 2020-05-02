import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import os
import subprocess 
import pathlib
import random
from sklearn.externals import joblib
#reading dataset 
color = "#%06x" % random.randint(0, 0xFFFFFF)
# plt.scatter(data['x'],data['y_act'],marker='o',c=colour[i])
data_original = pd.read_csv("dataset.csv")
plt.clf()
plt.scatter(data_original['x'],data_original['y'],label='No of Points:'+str(len(data_original)),marker='o',c=color)


def find_dir_n_files(dir_):
    file_list=os.listdir(str(dir_))
    return file_list

def verify_cluster():

    dir_ = './result/final_cluster_result/'
    files_ = find_dir_n_files(dir_)
    print('files_: ', files_)
    for i in range(len(files_)):
        print('i: ', i)
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        path_ = str(dir_)+str(files_[i] )
        print('path_: ', path_)
        data = pd.read_csv(path_)
        cluster_label = files_[i].split('_')[-2]
        plt.plot(data['x'],data['y_pred'],label='No of data:'+str(len(data))+' cluster: '+str(cluster_label) ,marker='x',c=color)
        plt.scatter(data['x'],np.zeros(data.shape[0]),marker='.',c=color)
        plt.xlabel('X variable')
        plt.ylabel('Y variable')
        # plt.legend()



    #######################################################
    ############ Plotting ref points n centroid ###########
    #######################################################
    centroid_dir = './object_file/final_centroid/'
    centroid_files = find_dir_n_files(centroid_dir)
    print('centroid_files: ', centroid_files)
    for i in centroid_files:
        print('i: ', i)
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        centroid = joblib.load(centroid_dir+str(i))
        label = i[:-4].split('_')[-1] #centroid cluster label
        plt.scatter(centroid,0,marker='s',c=color,s=100,label='Centroid of cluster'+str(label))

    ref_dir = './object_file/final_cluster_reference_points/'
    ref_files = find_dir_n_files(ref_dir)
    for i in ref_files:
        print('i: ', i)
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        label = i[:-4].split('_')[-1] #centroid cluster label
        ref_point = joblib.load(ref_dir+str(i))
        plt.scatter(ref_point,0,marker='*',c=color,s=100,)

    # plt.legend()
    plt.savefig('comparision_plot_final.eps')
    plt.show()


if __name__ == "__main__":
    verify_cluster()

