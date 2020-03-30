#########################  Data Transfer File  ##############################################
# This  file to grab the required columns for the dataset then by processing 
# the columns convert into required format, training - testing split, model learniong 
# and backward elimination
#############################################################################################

import numpy as np
import pandas as pd 
from Backward_elimination import Backward_elimination as BE
import time 
import random
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import copy
import statsmodels.formula.api as sm
import statsmodels.api as smapi
from sklearn.metrics import r2_score,mean_squared_error
import matplotlib.pyplot as plt
from result_check import result_check 
from select_feature import  select_feature 
from sklearn import metrics
from search_fileNcreate import search_fileNcreate as SF
from feature_after_elimination import feature_after_elimination
##Directory to export the file of combination of different files
dir_path = './../'

import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
# print('dir_path: ', dir_path)
sys.path.append(dir_path)


#Obtaining Path of directory 
dir_split = dir_path.split('/')
# print('dir_split: ', dir_split)
Main_folder_dir = ''
for i in range(len(dir_split)-1):
        Main_folder_dir += dir_split[i] + str('/')



def max_relative_error(y_train,y_train_pred):
        error = np.max(np.abs(y_train - y_train_pred)/np.abs(y_train))
        return error 


def regression(dataset,y,choice,curr_directory,level = 0,cluster_label=0,test_size_fraction=0.1,elimination=False,child_type='root',sl=0.05):
        '''
        This method will generate the dataset from required information so that 
        generated dataset will be compatible to apply machine learning algorithm.
        That dataset if further divided into training, testing and validation set.
        By applying algorithm it will predict the data and return Adjusted R^2 value,
        and summary of result obtained. Backpropagation is also applied here to remove
        unnecessary feature.

        Arguments : (dataset,y,choice(Flag),curr_directory)
        
        Pass the dataset in specified foramt as given in data folder.

        how to works:
        When data is passed to the method, data gets divided into two parts training and testing sets.
        Based on taining set object is generated after regression and prediction will be done on same object. 
        
        '''


        '''
        Checking Pairwise plot 
        '''
        # result_check.pairwise_plot(dataset)
        SF.check_directory(str(curr_directory)+'/result/')

        print('''
        ############################
                VIF checking
        ############################
        ''')
        '''
        Variation Inflation factor before data scaled
        '''
        result_check.VIF(dataset,curr_directory,child_type,cluster_label)


        ##splitting dataset 
        X_data = dataset.loc[:,:]
        # X_train, X_test, y_train, y_test = train_test_split(X_data, y, test_size=0.2, random_state=0)
        X_train, X_test, y_train, y_test = train_test_split(dataset, y, test_size=test_size_fraction,random_state=42)
        # print('X_train: ', X_train.shape)
        X_names = list(dataset.columns) 


        #featrue scaling after adding the ones 
        '''
        featurea scaling
        '''
        #checking directory 
        SF.check_directory(str(curr_directory)+'/object_file/')

        from sklearn.preprocessing import MinMaxScaler,RobustScaler,StandardScaler
        # scalar = MinMaxScaler().fit(X_train) #scalar object  Mimmax Scalar
        scalar = StandardScaler().fit(X_train) #scalar object  Standard Scalar
        ###if commented means not used
        # # X_train = scalar.transform(X_train)
        # # X_test = scalar.transform(X_test)
        

        # Fitting Multiple Linear Regression to the Training set

        from sklearn import metrics  #To get error metric
        print('''
        ##########################################################
        #     Ordinary Least Square Model And Back Elimination  #
        ##########################################################
        ''')

        #Generating list of headers with first column as constant of ones
        '''
        Removing features by back-eliminations and then by statically significant features ae obtained 
        by which again regressor is obtained for prediction.
        '''
        # Regression with Backward  Elimination
        '''
        Modified as after after back elimination certain columns are removed 
        '''
        X_train_modified, training_adj_r2,summary,X_names_modified = BE.BackwardElimination_P(X_train,X_test,y_train,y_test,X_names,cluster_label,curr_directory,child_type,sl=sl,elimination=elimination)
        
        ##Predictor for testing data 
        regressor_OLS_modified = sm.OLS(endog=y_train, exog=X_train_modified).fit()       #Regressor Obtained for testing 

        '''
        Storing Regressor object for testing of external set  
        '''
        #checking directory 
        SF.check_directory(str(curr_directory)+'/object_file/scalar/')
        SF.check_directory(str(curr_directory)+'/object_file/regressor/')
        SF.check_directory(str(curr_directory)+'/object_file/x_names/')
        # SF.check_file_existence(str(curr_directory)+'/result/check_comparisons.txt')

        ####object is stored
        # f = open(str(curr_directory)+'/result/check_comparisons.txt','a') #file open

        filename_scalar=  str(curr_directory)+'/object_file/scalar/scalar_'+str(cluster_label)+'_'+str(child_type)+'.sav'
        joblib.dump(scalar,filename_scalar)  

        #saving object for further prediction
        filename_regressor = str(curr_directory)+'/object_file/regressor/regressor_'+str(cluster_label)+'_'+str(child_type)+'.sav'
        joblib.dump(regressor_OLS_modified, filename_regressor)

        filename_xnames =  str(curr_directory)+'/object_file/x_names/xname_'+str(cluster_label)+'_'+str(child_type)+'.sav'
        joblib.dump(X_names_modified,filename_xnames)  

        # filename_xnames_without_const =  str(curr_directory)+'/object_file/x_names/xname_without_const'+str(cluster_label)+'.sav'
        # joblib.dump(X_names_without_constant,filename_xnames_without_const)  

        # f.write('\n'+str(X_names_modified)) 
        # f.close()

        # print('\n\nSummary to match : \n')
        summary_first = regressor_OLS_modified.summary(xname=X_names_modified)       
        # print(summary_first)

        y_train_pred = regressor_OLS_modified.predict(X_train_modified) #prediction of y_train by model to find out mse

        #relative error check 
        max_relative_error_training = max_relative_error(y_train,y_train_pred)
        
        print('''
        ###############################
        #ERROR CRITERIA  and R2 Result#
        ###############################
        ''')
        print('\nmax_relative_error_training: ', max_relative_error_training)
        print("\nTraining R2 :",regressor_OLS_modified.rsquared)
        print("\nTraining Adjusted R2 : ",regressor_OLS_modified.rsquared_adj)


        #checking directory 
        SF.check_directory(str(curr_directory)+'/result/console_output/'+str(child_type))
        SF.check_file_existence(str(curr_directory)+'/result/console_output/'+str(child_type)+'/output_result.txt')


        f = open(str(curr_directory)+"/result/console_output/"+str(child_type)+"/output_result.txt", "a")
        f.write("\n\n######################################################################################################################")
        f.write("\n\n######################################################################################################################")
        f.write("\n\nCluster Label: "+str(cluster_label))
        f.write("\n\n####################################################################")
        f.write("\n########################       OUTPUT     ##########################")
        f.write("\n####################################################################\n")
        f.write(str(summary))
        f.close()

        #open and read the file after the appending:
        f = open(str(curr_directory)+"/result/console_output/"+str(child_type)+"/output_result.txt", "a")

        
        '''
        Coefficients with names
        '''
        #coefficient with name dictionary 
        f.write('''
        ########################
        # RESULT  COEFFICIENT: #
        ########################
        ''')


        print('''
        ########################
        # RESULT  COEFFICIENT: #
        ########################
        ''')
        coefficient_dictionary  = dict()
        for i in range(len(regressor_OLS_modified.params)):
            print('\n',X_names_modified[i] ,': ', regressor_OLS_modified.params[i])
            f.write('\n'+str(X_names_modified[i])+':'+str(regressor_OLS_modified.params[i])+'\n')
            coefficient_dictionary[X_names_modified[i] ] =  round(regressor_OLS_modified.params[i],4)

        comparison(y_train,y_train_pred,curr_directory,cluster_label,'train_',child_type) #comparing result training set 
        ############################################################################################
        # Predicting for testing dataset so all the data points can be used for further processing #
        ############################################################################################
        X_test_modified = feature_after_elimination(X_test,X_names_modified)
        y_test_pred = regressor_OLS_modified.predict(X_test_modified)
        comparison(y_test,y_test_pred,curr_directory,cluster_label,'test_',child_type)
        Testing_Adj_r2 = r2_score(y_test_pred , y_test)

        

        ##########################################################################################
        # Predicting for whole dataset so all the data points can be used for further processing #
        ##########################################################################################
        '''
        dataset contains two more columns 'y_pred' and 'y_act' that's why returning back and it is also 
        useful for further analysis like tertiary/binary tree
        '''
        dataset_modified = feature_after_elimination(dataset,X_names_modified)
        dataset['y_pred'] = regressor_OLS_modified.predict(dataset_modified)
        dataset['y_act'] = y

        #writing to the file
        f.write('\n\n Maximum  Relative Error in Training : '+ str(max_relative_error_training))
        f.write("\n Training R2 :"+str(regressor_OLS_modified.rsquared))
        f.write("\nTraining Adjusted R2 : "+ str(regressor_OLS_modified.rsquared_adj))

        ##It is for TESTING SET
        f.write('\nTesting R2 :'+str(Testing_Adj_r2))
        # f.write('MSR_training :'+str(mean_squared_error(y_train,y_train_pred)))        
        # print('MSR_training :',mean_squared_error(y_train,y_train_pred))
        # print('MSR_testing :',mean_squared_error(y_test, y_test_pred))
        f.write('\nMSR_testing :'+str(mean_squared_error(y_test, y_test_pred)))

        f.close()
        
        return max_relative_error_training,training_adj_r2,Testing_Adj_r2,summary,coefficient_dictionary,dataset

def comparison(y_act,y_pred,curr_directory,cluster_label,file_name,child_label='root'):
        #comparison of data 
        SF.check_directory(str(curr_directory)+'/result/ID_comparison/'+str(child_label)+'/ID_comparison_'+str(cluster_label)+'/')
        #checking directory 
        ID_comparison = pd.DataFrame()
        y_act = np.array(y_act)
        ID_comparison['y_predicted'] = y_pred
        ID_comparison['y_actual'] = y_act
        ID_comparison['Relative Error'] = np.abs(y_pred - y_act)/np.abs(y_act)
        ID_comparison.to_csv(str(curr_directory)+'/result/ID_comparison/'+str(child_label)+'/ID_comparison_'+str(cluster_label)+'/ID_comparison_'+str(file_name)+str(cluster_label)+'.csv')
