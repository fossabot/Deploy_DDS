import pandas as pd
import numpy as np 
from Tertiary_Tree import Ternary_Tree as TT
from select_feature import select_feature
import os

##################################
############    Input    #########
##################################
dir_path = os.path.dirname(os.path.realpath(__file__))
data  = pd.read_csv('dataset.csv')
x = data['x']
y = data['y']
rel_error_criteria = 0.2
flag  = '-t'
curr_directory = dir_path
elimination = False
sl = 0.05

x,y = select_feature.feature_selection(data)  
Tree = TT(x,y,rel_error_criteria,flag,curr_directory,elimination=elimination,sl=sl)
Tree.Implement_Tree()
