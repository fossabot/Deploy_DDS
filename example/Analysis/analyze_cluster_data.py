import pandas as pd
import numpy as np
import os
import subprocess

import os

path = './result/final_cluster/' 
files = os.listdir(path)

files_csv = [i for i in files if i.endswith('.csv')]
files_csv.remove('full_data.csv')

all_data = pd.read_csv(str(path)+'full_data.csv')
for i in files_csv :
		cluster_i = pd.read_csv(str(path)+str(i))
		original_data_clu_i = all_data[all_data['Unnamed: 0'].isin(cluster_i['Unnamed: 0'])]
		original_data_clu_i.to_csv(str(path)+'cluster_'+str(i),index=False)

print('check  :',str(path))
