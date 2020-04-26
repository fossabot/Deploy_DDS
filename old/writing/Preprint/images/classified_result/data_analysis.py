import pandas as pd
import copy
import matplotlib.pyplot as plt
import shutil
import os


def makedir(dir):
    '''
    it generates the path 
    '''
    # define the name of the directory to be created
    path = "./result/"+str(dir)+'/'
    os.mkdir(path)
    return path


def find_strightchain_alkanes(Fuel_Name_data):
        '''
        This module will find only stright chain alkanes from the dataset
        and it 
        '''
        unique_fuels = list(Fuel_Name_data['Fuel'].unique())   #findind out all unique fuels               
        list_fuel = []  #List of fuels to store
        print(unique_fuels)
        for i in range(len(unique_fuels)):
            fuel_selected = unique_fuels[i]
            flag = 0
            for j in range(len(fuel_selected)):
                if(fuel_selected[j] == 'C'):
                    flag = 0
                else:
                    flag = 1
                    break
            if(flag == 0):
                list_fuel.append(fuel_selected)
        
        Data = copy.deepcopy(Fuel_Name_data)
        dataset = pd.DataFrame([])
        for i in range(len(list_fuel)):
                # print('Data.Fuel == list_fuel[i]: ', Data.Fuel == list_fuel[i])
                dataset = dataset.append(Data[Data.Fuel == list_fuel[i]]) #filetring dataset according list fuels
        dataset = dataset.reset_index(drop=True)        
        
        return dataset,list_fuel

def replace_nan_with_least(data):
    '''
    repalces least value with least value in the column
    '''
    least_temp_error = data['T_Error(%)'].dropna().min(skipna=True)
    data['T_Error(%)'] = data['T_Error(%)'].fillna(least_temp_error)
    data['T_Error(%)'] = data['T_Error(%)'].str.strip('')
    least_press_error = data['P_Error(%)'].dropna().min(skipna=True)
    data['P_Error(%)'] = data['P_Error(%)'].fillna(least_temp_error)
    data['P_Error(%)'] = data['P_Error(%)'].str.strip('')
    return data



def RemovePlusMinus(data):
    '''
    removes plus_minus symbol
    '''
    print(data['T_Error(%)'])
    data['T_Error(%)'] = data['T_Error(%)'].replace('±','',regex=True)
    data['P_Error(%)'] = data['P_Error(%)'].replace('±','',regex=True)
    return data
    

#read data
data  = pd.read_csv('Alkane_Dataset_.csv')
data = RemovePlusMinus(data)
data = replace_nan_with_least(data)
data.to_csv('check.csv')
#find alkanes
alkanes_data,uniq_fuel = find_strightchain_alkanes(data)
if(os.path.isdir('./result/')):
    shutil.rmtree('./result/')
    os.mkdir('result')
else:
    os.mkdir('result')

#printing data range its histogram
for i in range(len(uniq_fuel)):
            curr_dir = makedir(uniq_fuel[i])
            #removing pm symbol from 
            specific_fuel = alkanes_data[alkanes_data.Fuel == uniq_fuel[i]]  #filetring dataset according list fuels
            print('\n')
            print('uniq_fuel :',uniq_fuel[i])
            #TEMPERATURE FRQ
            plt.figure(10*i+0)
            plt.hist(specific_fuel['T(K)'])
            plt.savefig(str(curr_dir)+str(uniq_fuel[i])+'_temp.png')
            print('Maximum Temeprature : ',max(specific_fuel['T(K)']))
            print('Minimum Temeprature : ',min(specific_fuel['T(K)']))
            #TEMPERATURE uncertain
            plt.figure(10*i+5)
            plt.hist(specific_fuel['T_Error(%)'])
            plt.savefig(str(curr_dir)+str(uniq_fuel[i])+'_temp_err.png')
            print('Maximum Temeprature Error : ',max(specific_fuel['T_Error(%)']))
            print('Minimum Temeprature Error : ',min(specific_fuel['T_Error(%)']))
            
            #pressure
            plt.figure(10*i+1)
            plt.hist(specific_fuel['P(atm)'])
            plt.savefig(str(curr_dir)+str(uniq_fuel[i])+'_press.png')
            print('Maximum Pressure : ',max(specific_fuel['P(atm)']))
            print('Minimum Pressure : ',min(specific_fuel['P(atm)']))
            #Pressure uncertain
            plt.figure(10*i+0)
            plt.hist(specific_fuel['P_Error(%)'])
            plt.savefig(str(curr_dir)+str(uniq_fuel[i])+'_pressure_err.png')
            print('Maximum Pressure Error: ',max(specific_fuel['P_Error(%)']))
            print('Minimum Pressure Error: ',min(specific_fuel['P_Error(%)']))
            #Fuel
            plt.figure(10*i+2)        
            plt.hist(specific_fuel['Fuel(%)'])
            plt.savefig(str(curr_dir)+str(uniq_fuel[i])+'_fuel.png')

            print('Maximum Fuel% : ',max(specific_fuel['Fuel(%)']))
            print('Minimum Fuel% :',min(specific_fuel['Fuel(%)']))

            #oxidizer
            plt.figure(10*i+3)
            plt.hist(specific_fuel['Oxidizer(%)'])
            plt.savefig(str(curr_dir)+str(uniq_fuel[i])+'_oxi.png')
            print('Maximum Oxidizer% : ',max(specific_fuel['Oxidizer(%)']))
            print('Minimum Oxidizer% : ',min(specific_fuel['Oxidizer(%)']))

            #group
            plt.hist(specific_fuel['Research_group'])

            #Equivalecne Ratio
            plt.figure(10*i+4)
            plt.hist(specific_fuel['Equv(phi)'])
            plt.savefig(str(curr_dir)+str(uniq_fuel[i])+'_equi.png')
        
            print('Equv(phi): ',max(specific_fuel['Equv(phi)']))
            print('Equv(phi) : ',min(specific_fuel['Equv(phi)']))
            plt.close("all")

            print('Number of Datapoints:',len(specific_fuel))
            

            
