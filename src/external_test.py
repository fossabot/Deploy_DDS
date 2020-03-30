######################### External test File  ##############################################
# This  file will call external testset and based using saved object classify the data 
# into clusters using centroid and do regression on classified data
#############################################################################################

import numpy as np
import pandas as pd 
import time 
import random
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
 ###Heat Map###
# import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import copy
from data_gen import data_gen
import warnings
from find_fuel_type import find_fuel_type
from select_feature import select_feature
import subprocess
from search_fileNcreate import search_fileNcreate  as SF
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


class external_test():

        '''
        Checks new fuel which are not part of training or testing set
        '''
        def __init__(self,flag_value,curr_directory):
                self.flag_value = flag_value
                self.curr_directory = curr_directory
        


        def max_relative_error(self,y_train,y_train_pred):
                error = np.max(np.abs(y_train - y_train_pred)/np.abs(y_train))
                return error 


        def external_testset(self,external_data):
                '''
                Adding test set from external source to predict new fuel 
                '''
                #finding out the straight chain alkanes
                warnings.warn('Processing only with straight chain Alkanes')

                list_fuel = find_fuel_type.find_strightchain_alkanes(external_data)

                external_data_full = data_gen(external_data,list_fuel,self.flag_value)     #normal dataset generation

                df,tau = select_feature.feature_selection(external_data_full)
                
                #finding number of clusters and file names of cluster object 
                num_of_clusters, cluster_centroid_file_names, cluster_label = self.find_total_clusters()
                # print('cluster_centroid_file_names: ', cluster_centroid_file_names)
                print('cluster_label: ', cluster_label)

                # print('cluster_centroid_file_names: ', cluster_centroid_file_names)
                # print('no_of_clusters: ', num_of_clusters)

                #Classifying data based on clusters
                classified_df = self.assign_clusters_to_testdata(df,num_of_clusters,cluster_centroid_file_names,cluster_label)

                #Again joining the dependent value to the df, as it is easy to identify dependent variable when seperated by class
                df['Time(μs)'] = tau

                ###linear regression
                for i in range(num_of_clusters):
                        print('num_of_clusters: ', num_of_clusters)
                        #clustering process
                        #seperating data by class or cluster
                        cluster_dataframe = df[df['Class']  == cluster_label[i]] #cluster dataframe is obtained by single class
                        y_cluster = cluster_dataframe['Time(μs)']
                        cluster_dataframe_class = cluster_dataframe['Class']
                        cluster_dataframe = cluster_dataframe.drop(columns=['Time(μs)'])
                        cluster_dataframe = cluster_dataframe.drop(columns=['Class'])

                        #calling object files
                        regressor_OLS_modified = joblib.load(str(self.curr_directory)+'/object_file/regressor/regressor_'+str(cluster_label[i])+'.sav')
                        X_names_modified = joblib.load(str(self.curr_directory)+'/object_file/x_names/xname_'+str(cluster_label[i])+'.sav')
                        # scalar =  joblib.load(str(self.curr_directory)+'/object_file/scalar_'+str(cluster_label[i])+'.sav')
                        
                        #Dropping unnecessary features 
                        cluster_dataframe_header = list(cluster_dataframe.columns) 

                        # 1. first change drop the column which are not train set  by X_names
                        # 2. then transform the dataset #if any scalar is used


                        ###1.
                        for j in cluster_dataframe_header:
                                if(j not in X_names_modified ):
                                        cluster_dataframe = cluster_dataframe.drop(columns=j)
                                        # print('cluster_dataframe: ', cluster_dataframe.shape)
                        #transforming dataframe before adding one
                        #Generating list of headers with first column as constant of ones

                        # ###2. commented if no cluster is used
                        # cluster_dataframe = scalar.transform(cluster_dataframe)



                        #As Testing of all data points, all data points are assigned to the X_test_external
                        #testing to make compatible with dataframe 
                        X_train_external, X_test_external, y_train_external, y_test_external = train_test_split(cluster_dataframe, y_cluster, test_size=0.99999, shuffle=False)
                        # print('X_test_external: ', X_test_external)
                        # print(regressor_OLS_modified.params)

                        y_pred = regressor_OLS_modified.predict(X_test_external)
                        cluster_dataframe['Class'] = cluster_dataframe_class
                        cluster_dataframe['Time(μs)_actual'] = y_test_external
                        cluster_dataframe['Time(μs)_predicted'] = y_pred
                        # result = loaded_model.score(X_test, Y_test)

                        SF.check_directory(str(self.curr_directory)+'/external_test_result/console_output/') #checking directory
                        SF.check_directory(str(self.curr_directory)+'/external_test_result/classified_data/') #checking directory
                        SF.check_file_existence(str(self.curr_directory)+"/external_test_result/console_output/output_result.txt")
                        cluster_dataframe.to_csv(str(self.curr_directory)+'/external_test_result/classified_data/classified_cluster'+str(cluster_label[i])+'.csv')
                        f = open(str(self.curr_directory)+"/external_test_result/console_output/output_result.txt", "a")
                        
                        ##########################################################
                        ###################  Result ##############################
                        ##########################################################

                        #resettign index
                        try:
                                y_pred = y_pred.reset_index(drop=True)
                                y_test_external = y_test_external.reset_index(drop=True)                                
                        except AttributeError:
                                pass
                        
                        ###printing result
                        print('Result for cluster-',str(cluster_label[i]),':\n')
                        f.write('\n Result for cluster-'+str(cluster_label[i])+':\n')
                        print('\n Index','          ','Y_actual','            ','Y_Predicted','                ','Relative Error')
                        f.write('\n Index'+'          '+'Y_actual'+'            '+'Y_Predicted'+'                '+'Relative Error')
                        for k in range (len(y_pred)):
                                # print(fuel_name[k],'            ',np.log(y_given[k]),'  ',y_test_external[k],'      ',y_pred[k],'    ',np.abs(y_test_external[k]-y_pred[k])/y_test_external[k],'\n')
                                print(k ,': ', y_test_external[k],'      ',y_pred[k],'    ',np.abs(y_test_external[k]-y_pred[k])/np.abs(y_test_external[k]),'\n')
                                f.write('\n'+str(k) +': '+ str(y_test_external[k])+'      '+str(y_pred[k])+'    '+str(np.abs(y_test_external[k]-y_pred[k])/np.abs(y_test_external[k]))+'\n')                        
                        ## result comparison and save
                        ID_comparison = pd.DataFrame()
                        ID_comparison['y_predicted'] = y_pred
                        ID_comparison['y_actual'] = y_test_external
                        ID_comparison['Relative Error'] = np.abs(y_pred - y_test_external)/np.abs(y_test_external)
                        SF.check_directory(str(self.curr_directory)+'/external_test_result/Ignition_delay_comparison/') #checking directory
                        ID_comparison.to_csv(str(self.curr_directory)+'/external_test_result/Ignition_delay_comparison/ID_comparison_external_cluster_'+str(cluster_label[i])+'.csv')
                        maximum_relative_error_external = self.max_relative_error(y_test_external,y_pred)
                        print('\n\n Maximum Relative Error in external data for cluster-',str(cluster_label[i]),' :',maximum_relative_error_external)
                        f.write('\n\n Maximum Relative Error in external data for cluster-'+str(cluster_label[i])+' :'+str(maximum_relative_error_external))
                        f.close()

                        #############
                        # PLOTTING  #
                        #############

                        #Drawing line at 45 
                        x = np.arange(-15,15,0.5)

                        '''
                        plot of external test set result 
                        '''
                        SF.check_directory(str(self.curr_directory)+'/external_test_result/prediction_comparison_plots/') #checking directory
                        plt.clf()
                        plt.plot(x,x,linestyle='--',color='black')
                        plt.scatter(y_pred, y_test_external, s=20, cmap='viridis',label= str('Cluster-'+str(cluster_label[i]).replace('_',' \{')+' cluster\} data points'))
                        text = "Maximum Relative Error : "+ str(maximum_relative_error_external)
                        plt.xlim([2,11])
                        plt.ylim([2,11])
                        plt.rc('text', usetex=True)
                        plt.xlabel('Predicted IDT ')
                        plt.ylabel('Actual IDT')
                        plt.tick_params(axis='both', which='major', labelsize=12)
                        plt.text(3,0,text,)
                        plt.tight_layout()
                        plt.legend(loc='lower right',handlelength=1, borderpad=1.2, labelspacing=0.5,framealpha=0.5,fontsize=12)
                        plt.savefig(str(self.curr_directory)+'/external_test_result/prediction_comparison_plots/ignition_delay_external_'+str(cluster_label[i])+'.eps', format='eps', dpi=600)
                       
                # plt.show()
                plt.close()
        
        def find_total_clusters(self):
                '''
                This method will find out number of cluster based on center nodes saved on the 
                '''
                #counting number files in the centroid directory which is total number of centroids
                directory_path = str(self.curr_directory)+'/object_file/centroids/'
                cmd_num_of_files = "find "+directory_path+" -type f | wc -l"
                #check_output return output of bash 
                num_of_cluster = int(subprocess.check_output(cmd_num_of_files,shell=True, universal_newlines=False))  # returns the exit code in unix

                #finding name of files in the centroid directory
                cmd_files_name = "ls "+directory_path
                centroid_file_names = str(subprocess.check_output(cmd_files_name,shell=True, universal_newlines=False),"utf-8").split('\n') #converting output into string and then splitting 
                file_names = [] #storing  file names
                file_name_label = []
                for i in range(len(centroid_file_names)-1):
                        file_names.append(centroid_file_names[i]) #storing file labels
                        file_name_label.append(centroid_file_names[i][:-4].split('_')[-2]+'_'+centroid_file_names[i][:-4].split('_')[-1]) #storing centroid index -- cluster label #useful for other file reading
                # file_names = file_names.sort()
                print('file_names: ', file_names)
                return num_of_cluster,file_names,file_name_label
        
        def assign_clusters_to_testdata(self,data,num_of_centroids,cluster_centroid_file_names,cluster_label):
                '''
                num_of_clusters = num_of_centroids
                calculating distance of data point from all the available centroid and appending the 
                calculated values from all clusters to new dataset - distance_from_centroids to find out the 
                least distance from the centroid and further classification is done and class name is same as 
                centroid name
                '''
                data_centroid = copy.deepcopy(data) #data processed for calculation assignment of centroid
                data_centroid = data_centroid.drop(columns=['Constant'])

                #finding distance from the centroid 

                distance_from_centroids = pd.DataFrame([]) #converting into pandas DataFrame

                for i in range(num_of_centroids): #for all clusters
                        centroid = joblib.load(str(self.curr_directory)+'/object_file/centroids/'+cluster_centroid_file_names[i])
                        #calculating euclidian distacne for all data points from each cluster
                        distance_from_centroid = []
                        for j in range(len(data_centroid)): #for all data points
                                calculated_distance = self.euclidian_dist(data_centroid.loc[j,:],centroid) #calling function
                                distance_from_centroid.append(calculated_distance)
                        distance_from_centroids[cluster_label[i]] = distance_from_centroid

                #finding index of the minimum values and appending to the main dataframe
                data_class = distance_from_centroids.idxmin(axis=1)
                # print('data_class: ', data_class)

                # Assigning centroid to the data 
                # note: data class is assigned based on centroid class
                data['Class'] = data_class #rather than asssigning number centroid name is assigned to the class

                # data.to_csv('check_testset_clus.csv')
                
                return data

        def euclidian_dist(self,arr_1,arr_2):
                arr_1 = np.array(arr_1)
                arr_2 = np.array(arr_2)
                '''
                calculating distance by passed row of matrix and centroid 
                '''
                distance = np.linalg.norm(arr_1-arr_2)
                return distance


if __name__ == "__main__": 
        external_data = pd.read_csv(str(Main_folder_dir)+'/data/test_set/test_dataset.csv')
        external_test.external_testset(external_data)
        # #manual result 
        # # cluster_result_format = ['intercept','Temp','pressure','fuel','oxygen','P_S','S_S','P_H','S_H']
        # cluster_0_coef ={'Constant':36.68,'Temp(K)':-15.99,'log_P(atm)':-0.55,'log_Fuel(%)':0.94, 'log_Oxidizer(%)':-1.69,'P_S':-0.28,'S_S':0.13,'P_H' :-0.84,'S_H' :0}
        # cluster_1_coef = {'Constant':32.96,'Temp(K)':-15.08,'log_P(atm)':-0.44,'log_Fuel(%)':0.68, 'log_Oxidizer(%)':-1.12,'P_S':-0.05,'S_S':0.29,'P_H' :-0.16,'S_H' :0}
        # cluster_2_coef ={'Constant':101.85,'Temp(K)':-42.46,'log_P(atm)':-1.04,'log_Fuel(%)':-0.14, 'log_Oxidizer(%)':-0.34,'P_S':-6.42,'S_S' :2.55,'P_H' :-19.26,'S_H': -1.31}
        # # cluster_2_coef ={'Constant':103.3123,'Temp(K)':-43.203,'log_P(atm)':-1.0753,'log_Fuel(%)':-0.225, 'log_Oxidizer(%)':-0.2724,'P_S':-6.4955,'S_S' :2.568,'P_H' :-19.4865,'S_H': -1.3595}

        # all_cluster_coef = ([cluster_0_coef,cluster_1_coef,cluster_2_coef])
        # external_test.manual_testing(external_data,all_cluster_coef)
