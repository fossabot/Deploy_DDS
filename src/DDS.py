'''
This is kind of main method for all .py files
this files control all other files and controlled 
by shell script
'''

#tracking Current directory 
import os
current_directory  = os.getcwd()
# print('current_directory: ', current_directory)

#Addding all files from src to system default directory 
import sys
sys.path.insert(0, str(current_directory)+'/src')
from Flag import Flag
from search_fileNcreate import search_fileNcreate as SF
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


########################Change the data here #########################
arguments_len = len(sys.argv)
print('arguments_len: ', arguments_len)
flag = sys.argv[1]
if(flag == '-b'):
    smile = sys.argv[2]
else:
    dataset_location = sys.argv[2]
curr_directory = sys.argv[3]
print('curr_directory: ', curr_directory)
######################################################################

#cleaning output file
SF.check_directory(str(curr_directory)+"/result" ) #checking directory
SF.check_file_existence(str(curr_directory)+"/result/output_result.txt") #checking file existence
f = open(str(curr_directory)+"/result/output_result.txt", "w")
f.write('')
f.close()


if(flag == '-t' or flag == '-o'):
    #arguments passed by Run.sh
    #error based tree criteria 
    error_criteria_to_divide = float(sys.argv[4])
    #elimination criteria 
    elimination = sys.argv[5]
    elimination = True if elimination=='True' else False
    #backward elimination significance criteria 
    sl = float(sys.argv[6])
    #If you want to use significance level
    limited_ref_points = sys.argv[7]
    if(limited_ref_points == 'True' or limited_ref_points == 'False'):
        limited_ref_points = True if limited_ref_points=='True' else False
    Flag.switch_func(flag,dataset_location=dataset_location,curr_directory=curr_directory,division_error_criteria=error_criteria_to_divide,elimination=elimination,sl=sl,limited_ref_points=limited_ref_points) 

elif(flag == '-m'):
    elimination=sys.argv[4]
    sl = sys.argv[5]
    Flag.switch_func(flag,dataset_location=dataset_location,curr_directory=curr_directory,elimination=elimination,sl=sl)
    
elif(flag != '-b' and flag != '-t'):
    Flag.switch_func(flag,dataset_location=dataset_location,curr_directory=curr_directory) 
if(flag == '-b'):
    Flag.switch_func(flag,curr_directory=curr_directory,smile=smile) 