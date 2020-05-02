#tracking Current directory 
import os
current_directory  = os.getcwd()
# print('current_directory: ', current_directory)

#Addding all files from src to system default directory 
import sys
sys.path.insert(0, str(current_directory)+'/src')

import os
import rdkit as Chem 
import numpy as mp
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
# print('dir_path: ', dir_path)
sys.path.append(dir_path)
sys.path.append(dir_path+str('/clustering_methods'))


#Obtaining Path of directory 
dir_split = dir_path.split('/')
# print('dir_split: ', dir_split)
Main_folder_dir = ''
for i in range(len(dir_split)-1):
    Main_folder_dir += dir_split[i] + str('/')

class search_fileNcreate():
    def check_file_existence(file_name=None):
        # print('file_name: ', file_name)
        file_dir = str(file_name)
        try:
            os.mknod(file_dir)
            # print('\n File does not exist so, created!\n')
        except FileExistsError:
            # print('\n File already exist!')
            pass
    
    def check_directory(folder_name=None):
        try:
            os.makedirs(folder_name)
            # print('\n Directory does not exist so, created!\n')
        except FileExistsError:
            # print('\n Directory already exist!\n ')     
            pass       

if __name__ == "__main__":
    print(os.system('pwd'))
    search_fileNcreate.check_file_existence("result/bond_detail.csv")
