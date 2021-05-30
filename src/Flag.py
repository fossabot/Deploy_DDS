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
 

    def switch_func(Flag_value,dataset_location=None,curr_directory=None,smile=None,division_error_criteria=0.05,elimination=False,sl=0.05,limited_ref_points=False):
        '''
        This methos works like switch in c++.
        According to your Flag it will divert the code and 
        process the code given Flag values.
        Argument Passed :(value)
        
        value is digit of your Flag dislayed in Flag method.
        Here, value is coming from Flag method.
        '''
        #Adding library 
        try:
            '''
            If  externally features are supplied given more priority
            '''
            sys.path.append(curr_directory)
            from feature_selection import select_feature as Sel_feat
        except:
            from select_feature import select_feature as Sel_feat

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
            Bond_details = BE.Bond_Extract(smile_input,curr_directory)
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

            dataset = data_gen(Fuel_data,list_fuel,Flag_value,curr_directory)     #normal dataset generation
            df,tau = Sel_feat.feature_selection(dataset)

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
                from Ternary_Tree import Ternary_Tree as TT
                from combine_clusters import combine_clusters as CC

                #finding out the straight chain alkanes
                list_fuel = find_fuel_type.find_strightchain_alkanes(Fuel_data)

                dataset = data_gen(Fuel_data,list_fuel,Flag_value,curr_directory)     #normal dataset generation
                SF.check_directory(str(curr_directory)+'/result/final_cluster/')
                dataset.to_csv(str(curr_directory)+'/result/final_cluster/full_data.csv')

                df,tau = Sel_feat.feature_selection(dataset)

                # df.to_csv(str(curr_directory)+'/Transformed.csv')
                print('division_error_criteria: ', division_error_criteria)
                Tree = TT(df,tau,division_error_criteria,Flag_value,curr_directory,elimination=elimination,sl=sl,limited_ref_points=limited_ref_points)
                
                Tree.Implement_Tree()
                # genefaring original cluster wise data 
                from analyze_cluster_data import analyze_cluster_data
                analyze_cluster_data(curr_dir=curr_directory)

                # #Training Result Analyzer
                # print('\n\n\ntraining_accuracy')
                # from training_accuracy_check import training_accuracy_check
                # train_accu = training_accuracy_check(Flag_value,curr_directory)
                # train_accu.training_accuracy(dataset)


                # #optimizing cluster
                # final_clusters = CC(curr_directory,division_error_criteria,Flag_value)
                # final_clusters.optimize_cluster()

                print('\n\n Executed Normally! Please check plot Folder')
                # os.system('sh ./for_ploting.sh')

        elif(Flag_value == '-d'):
                '''
                gives Transformed data
                '''
                from data_gen import data_gen
                external_data = pd.read_csv(dataset_location)
                list_fuel = find_fuel_type.find_strightchain_alkanes(external_data)
                dataset = data_gen(external_data,list_fuel,Flag_value,curr_directory)     #normal dataset generation
                df,tau = Sel_feat.feature_selection(dataset)
                df['Time'] = tau
                df.to_csv(str(curr_directory)+'/tranformed_data.csv',index=False)
   
        elif(Flag_value == '-e'):
                '''
                External test-cases
                '''
                from data_gen import data_gen
                external_data = pd.read_csv(dataset_location)
                list_fuel = find_fuel_type.find_strightchain_alkanes(external_data)
                dataset = data_gen(external_data,list_fuel,Flag_value,curr_directory)     #normal dataset generation

                #old
                from old_external_test import old_external_test
                testset_obj_old = old_external_test(Flag_value,curr_directory)
                testset_obj_old.external_testset(dataset)

                # # new
                # from external_test import external_test 
                # testset_obj = external_test(Flag_value,curr_directory)
                # testset_obj.external_testset(dataset)
                # print('\n\n Executed Normally! Please check plot Folder')

        elif(Flag_value == '-k'):
        	
                '''
                External test-cases
                By this flag can be used to store all the prediction result
                '''
                from data_gen import data_gen
                external_data = pd.read_csv(dataset_location)
                list_fuel = find_fuel_type.find_strightchain_alkanes(external_data)
                dataset = data_gen(external_data,list_fuel,Flag_value,curr_directory)     #normal feature generation

                #old
                from old_external_test_cycle import old_external_test_cycle
                testset_obj_old = old_external_test_cycle(Flag_value,curr_directory)
                testset_obj_old.external_testset(dataset)

        elif(Flag_value == '-f'):

                from combined_N_analyze_all_test_result import combined_N_analyze_all_test_result
                combined = combined_N_analyze_all_test_result(curr_directory)
                combined.process()

                
        elif(Flag_value == '-p'):
                '''
                Plot of average coefficient value obtained by histogram of coefficients
                '''
                print(dataset_location)
                coef_data = pd.read_csv(dataset_location)       
                from coefficient_plotting import coefficient_plotting as CP 
                weights_mean_n_header = CP.coefficient_mean_result_density(coef_data,curr_directory)
                print('\n\n Executed Normally! Please check plot Folder')
        
        elif(Flag_value == '-o'):
                '''
                This Flag is same as three but before transferring the data to find out R2,
                Data has to be transferred to tree structure and divide the data in middle way.
                Add tree module without uncertainty
                '''

                print("## Tree Structure and data division for non-fuel data only## \n")
                dataset = pd.read_csv(dataset_location)
                
                from data_gen import data_gen
                from Ternary_Tree import Ternary_Tree as TT
                from combine_clusters import combine_clusters as CC

                
                df,tau = Sel_feat.feature_selection(dataset)
                df.to_csv(str(curr_directory)+'/Transformed.csv',index=False)
                Tree = TT(df,tau,division_error_criteria,Flag_value,curr_directory,elimination=elimination,sl=sl,limited_ref_points=limited_ref_points)
                Tree.Implement_Tree()
            
                # #optimizing cluster
                # final_clusters = CC(curr_directory,division_error_criteria,Flag_value)
                # final_clusters.optimize_cluster()

                #old
                from data_gen import data_gen
                external_data = pd.read_csv(str(curr_directory)+'/testset.csv')

                from old_external_test import old_external_test
                testset_obj_old = old_external_test(Flag_value,curr_directory)
                testset_obj_old.external_testset(external_data)

                # # new
                # from external_test import external_test 
                # testset_obj = external_test(Flag_value,curr_directory)
                # testset_obj.external_testset(external_data)

                print('\n\n Executed Normally! Please check plot Folder')
                # os.system('sh ./for_ploting.sh')
