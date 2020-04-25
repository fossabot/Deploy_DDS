##############################################################
#              To take input of your Flag                  #
##############################################################

#Note: curre_dir : /home/pragnesh/Git/Data_driven_Kinetics/CleanCode/testing_place 
#does not contain / in the end 


import sys
import os 
import pandas as pd
import numpy as np
from find_fuel_type import find_fuel_type 
from search_fileNcreate import search_fileNcreate as SF
from select_feature import select_feature
dir_path = os.path.dirname(os.path.realpath(__file__))
# print('dir_path: ', dir_path)
sys.path.append(dir_path)
# sys.path.append(dir_path+str('/clustering_methods'))


#Obtaining Path of directory 
dir_split = dir_path.split('/')
# print('dir_split: ', dir_split)
Main_folder_dir = ''
for i in range(len(dir_split)-1):
    Main_folder_dir += dir_split[i] + str('/')

    
    
class Flag():
    '''
    This class method for Flags and diverts the code accordingly 
    '''
 

    def switch_func(Flag_value,dataset_location=None,curr_directory=None,smile=None,division_error_criteria=0.05,elimination=False,sl=0.05):
        '''
        This methos works like switch in c++.
        According to your Flag it will divert the code and 
        process the code given Flag values.
        Argument Passed :(value)
        
        value is digit of your Flag dislayed in Flag method.
        Here, value is coming from Flag method.
        '''

        #Calling dataset 

        if (Flag_value == '-a'):
            #importing library 
            from Data_analysis import Data_analysis 
            Data_analysis.View_n_Analyze(dataset_location,curr_directory) #calling method to generate analyze the dataset 
            print('\n\n Check directory ./result/data_analysis/')

        elif (Flag_value == '-b'):
            '''
            Smile base bond information 
            '''
            print('Finding the bond details')
            #importing library 
            from Bond_Extraction import Bond_Extraction as BE
            smile_input = [str(smile)]	#Argument List 
            Bond_details = BE.Bond_Extract(smile_input)
            print(Bond_details)
            SF.check_directory(str(curr_directory+'/result/Bond_details/'))
            SF.check_file_existence(str(curr_directory)+'/result/Bond_details/SMILE_result.csv')
            #reading old bond details
            try:
                Bond_dataframe = pd.read_csv(str(curr_directory)+'/result/Bond_details/SMILE_result.csv')
                Bond_details = pd.concat([Bond_dataframe,Bond_details]) #Concatenating two dataframes
            except pd.errors.EmptyDataError:
                pass
            #appending new data
            Bond_details.to_csv(str(curr_directory)+'/result/Bond_details/SMILE_result.csv',index=False)
            
            print('\n\n Check directory ./result/Bond_details/')

        elif(Flag_value == '-h'):
            '''
            Fuel analysis 
            This flag will analyze the fuel data and generate histogram plots of properties based on different fuels
            '''
            print("## You are going to proceed for All straight chain alkanes fuel available in the dataset ## \n")
            Fuel_data = pd.read_csv(dataset_location)
            from fuel_analysis import fuel_analysis #calling fuela analysis part
            fuel_analysis.fuel_data_analysis(Fuel_data,curr_directory)     #passing thw whole dataset to it 

        elif(Flag_value == '-m'):
            '''
            straight chain alkanes
            '''

            print("## You are going to proceed for All straight chain alkanes fuel available in the dataset ## \n")
            Fuel_data = pd.read_csv(dataset_location)

            from data_gen import data_gen
            #finding out the straight chain alkanes
            list_fuel = find_fuel_type.find_strightchain_alkanes(Fuel_data)

            dataset = data_gen(Fuel_data,list_fuel,Flag_value)     #normal dataset generation
            df,tau = select_feature.feature_selection(dataset)

            # #######################
            # # generate_data_points#
            # #######################
            # from generate_data_points import generate_data_points as GDP
            # extended_dataset = GDP.generate_dataset(datastet,Flag_value)

            # ###########
            # # equisize#
            # ###########
            # from equilize_dataset import equilize_dataset
            # equisize_dataset , Diff_dataset   = equilize_dataset(datastet,Flag_value) 
            # #equisized dataset returns,
            # #equisized_dataset -- have equal datapoints of all fuel w.r.t to least data available for any fuel 
            # #Diff_datset -- the remaining data points after equi-sizing tha dataset  --- use as testing
            
            from regression import regression as reg
            print('elimination',elimination)
            max_relative_error_training,training_adj_r2,Testing_Adj_r2,summary,coefficient_dictionary,dataset = reg(df,tau,list_fuel,curr_directory,elimination,sl=sl)
            print('\n\n Executed Normally! ')
    
        elif(Flag_value == '-t'):
                '''
                This Flag is same as three but before transferring the data to find out R2,
                Data has to be transferred to tree structure and divide the data in middle way.
                Add tree module without uncertainty
                '''

                print("## Tree Structure and data division for alkanes only## \n")
                Fuel_data = pd.read_csv(dataset_location)

                from data_gen import data_gen
                from Tertiary_Tree import Ternary_Tree as TT
                from combine_clusters import combine_clusters as CC

                #finding out the straight chain alkanes
                list_fuel = find_fuel_type.find_strightchain_alkanes(Fuel_data)

                dataset = data_gen(Fuel_data,list_fuel,Flag_value)     #normal dataset generation

                df,tau = select_feature.feature_selection(dataset)

                # df.to_csv(str(curr_directory)+'/Transformed.csv')

                Tree = TT(df,tau,division_error_criteria,Flag_value,curr_directory,elimination=elimination,sl=sl)
                Tree.Implement_Tree()
                
                #optimizing cluster
                final_clusters = CC(curr_directory,division_error_criteria,Flag_value)
                final_clusters.optimize_cluster()

                print('\n\n Executed Normally! Please check plot Folder')
                # os.system('sh ./for_ploting.sh')
   
        elif(Flag_value == '-e'):
                '''
                External test-cases
                '''
                from data_gen import data_gen
                from external_test import external_test 
                external_data = pd.read_csv(dataset_location)
                list_fuel = find_fuel_type.find_strightchain_alkanes(external_data)
                dataset = data_gen(external_data,list_fuel,Flag_value)     #normal dataset generation
                testset_obj = external_test(Flag_value,curr_directory)
                testset_obj.external_testset(dataset)
                print('\n\n Executed Normally! Please check plot Folder')
                
        elif(Flag_value == '-p'):
                '''
                Plot of average coefficient value obtained by histogram of coefficients
                '''
                print(dataset_location)
                coef_data = pd.read_csv(dataset_location)       
                from coefficient_plotting import coefficient_plotting as CP 
                weights_mean_n_header = CP.coefficient_mean_result(coef_data,curr_directory)
                print('\n\n Executed Normally! Please check plot Folder')


