'''
This method will generate extract bond details and add those column to the 
main dataset.
'''
##Directory to export the file of combination of different files
dir_path = './../'

import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)


#Obtaining Path of directory 
dir_split = dir_path.split('/')
Main_folder_dir = ''
for i in range(len(dir_split)-1):
        Main_folder_dir += dir_split[i] + str('/')
    


# Importing the libraries
import numpy as np
import pandas as pd
import time
import copy
from Bond_Extraction import Bond_Extraction as BE
import os
import time
import subprocess
from select_feature import select_feature 

def data_gen(Data,list_fuel,choice_value):
        '''
        Based on provided unique fuel choices, this method will ONLY generate the dataset.
        Arguments: (list_fuel)

        Pass the list of UNIQUE fuels(SMILES) as array. It will search given SMILES in the Dataset and based on that 
        value it will filter out all the data and make sub_dataset. It will repeat the process for all the Unique SMILEs
        and by appending all sub_dataset it will generate final dataset. It also generated the remaining information like
        Bond information and carbon_type and also append those columns to the dataset.
        '''
        # Importing the dataset
        dataset = pd.DataFrame([])
        for i in range(len(list_fuel)):
                # print('Data.Fuel == list_fuel[i]: ', Data.Fuel == list_fuel[i])
                dataset = dataset.append(Data[Data.Fuel == list_fuel[i]]) #filetring dataset accordinh list fuels
        dataset = dataset.reset_index(drop=True)        
        # print('dataset: ', dataset)
        ########## Passing information by Processing on smile file ##########

        # Information about  Type of carbon and Bond between Type of Carbon
        Fuel_Bonds = BE.Bond_Extract(list_fuel)
        # print('Fuel_Bonds: ', Fuel_Bonds)
        # print('Fuel_Bonds: ', list(Fuel_Bonds['Fuel']))

        Unique_fuel_name = list_fuel
        #column names
        columns = select_feature.bond_extraction_cols()

        #Empty Dataframe
        Extracted_bond_data = pd.DataFrame(columns=columns)

        #Generating data for all entries by unique entries
        for i in range(len(dataset)):
                if(list(dataset['Fuel'])[i] in list(Fuel_Bonds['Fuel'])): #grabbing index 
                        #capturing index of Fuel_Bonds matched by dataset index
                        #inshort capturing appropriate entry in fuel_bonds
                        Fuel_Bonds_index = list(Fuel_Bonds['Fuel']).index(list(dataset['Fuel'])[i])  
                        # To capture row from Fuel and save it into array
                        temp_list = Fuel_Bonds.iloc[Fuel_Bonds_index, :]
                        temp_list = pd.Series(temp_list)
                        Extracted_bond_data = Extracted_bond_data.append(temp_list, ignore_index=True)
                        # print('temp_list',temp_list)
                #Making equivalent_dataset of dataset size so we can combine
        # print(Extracted_bond_data)

        # Merging Two dataset, It will merge automatically by its common

        for i in range(len(columns)):
                dataset[columns[i]] = Extracted_bond_data[columns[i]]
        # dataset.to_csv('kmeans_kdataset.csv')
        return dataset

