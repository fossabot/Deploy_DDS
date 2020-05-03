import pandas as pd
import numpy as np 
from Tertiary_Tree import Ternary_Tree as TT
from select_feature import select_feature
import os
from combine_clusters import combine_clusters as CC
##################################
############    Input    #########
##################################
dir_path = os.path.dirname(os.path.realpath(__file__))
data  = pd.read_csv('dataset.csv')

x = data.iloc[:,:-1]
y = data.iloc[:,-1]
rel_error_criteria = 0.15
opt_criteria = 0.05
flag  = '-t'
curr_directory = dir_path
elimination = False
sl = 0.5

x,y = select_feature.feature_selection(data)  
Tree = TT(x,y,rel_error_criteria,flag,curr_directory,elimination=elimination,sl=sl)
Tree.Implement_Tree()

# #generating plot after tree
# from original_verify_result import *
# after_tree_plot()

# #optimizing cluster
# opt_cluster = CC(dir_path,opt_criteria,flag,)
# opt_cluster.optimize_cluster()

# #generating plot after tree
# from verify_result import *
# verify_cluster()

# #external testing 
# from external_test import external_test
# external_data = pd.read_csv('testset.csv')

# #old
# from old_external_test import old_external_test
# testset_obj = old_external_test('-t',curr_directory)
# testset_obj.external_testset(external_data)

# #new
# # from external_test import external_test 
# testset_obj = external_test('-t',curr_directory)
# testset_obj.external_testset(external_data)