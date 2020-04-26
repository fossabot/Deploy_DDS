import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as spt
import os
butane = 'Butane'
decane_sarthy = 'decane_sarthy'
dodecane = 'Dodecane'
dodecane_sarthy = 'dodecane_sarthy'
Heptane_sarthy = 'Heptane_sarthy'
Hexane = 'Hexane'
Nonane_sarthy = 'Nonane_sarthy'
octane_sarthy = 'octane_sarthy'
pentane = 'Pentane'
propane = 'Propane'
undocane_sarthy = 'undocane_sarthy'
heptane = 'Heptane'
# folder_list = [butane,decane_sarthy,propane,Hexane,dodecane,dodecane_sarthy,Heptane_sarthy,Nonane_sarthy,octane_sarthy,pentane,heptane]
folder_list = [butane,Hexane,pentane,propane,heptane]

#dataframe for the activation and file
Ea_by_R =  pd.DataFrame([])

fuel_list = []
intercepts_list =[]
EaR_list =[]

def temp_ID(foldername1):
    '''
    It will find the ignition delay and temp from the 
    Flamemaster format 
    '''
    #result 
    data =  pd.read_csv('./'+str(foldername1)+'/IgniDelTimesCHmax.dout',sep="\t")
    temp = []
    ID = []
    for i in range(1,data.shape[0],1):
        line = str(data.iloc[i,:]).split(' ') #reading line
        
        ID_time = line[4].split('\n')[0] #sepearting ID

        #TEMP SEPERATED
        Temp = str(line[5].split('(')[1])
        Temp = Temp.split(',')[0]
        
        ID.append(float(ID_time))
        temp.append(1000/float(Temp))
    return ID,temp

def regression(temp,ID):
    '''
    Regression form the given the limits
    '''
    # #regression
    #tau =  exp (Ea/R * 1/T)
    #log(tau) = Ea/R * 1/T
    slope, intercept, r_value, p_value, std_err = spt.linregress(temp,np.log(ID))
    print('std_err: ', std_err)
    print('p_value: ', p_value)
    print('r_value: ', r_value)
    print('intercept: ', intercept)
    print('slope: ', slope)
    return intercept, slope
    


files = os.listdir('./chemkin/')

for i in range(len(folder_list)):
    ID , temp = temp_ID(folder_list[i])
    ID = ID[14:25]
    temp = temp[14:25]
    plt.semilogy(temp,ID,marker='o',label = '$Fuel = %s ,P=5atm , X_{Fuel}=1, X_{Oxi}=Stochio, X_{Ar}=Rest$'%folder_list[i])
    intercept,slope = regression(temp,ID)

    fuel_list.append(folder_list[i])
    intercepts_list.append(intercept)
    EaR_list.append(slope)

    x = np.linspace(np.min(temp),np.max(temp),100)
    y = np.exp(intercept + (x  * slope))
    # plt.semilogy(x,y,linestyle='dashed',label = 'Regression line %s $Ea/R=%f$' %(folder_list[i],slope))

for i in range(len(files)):
    data  = pd.read_csv('./chemkin/'+str(files[i]))
    ID  = data.iloc[14:25,1] *1000
    print('ID: ', ID)
    temp = data.iloc[14:25,0]
    print('temp: ', temp)

    intercept,slope = regression(temp,ID)

    fuel_list.append(files[i])
    intercepts_list.append(intercept)
    EaR_list.append(slope)

    x = np.linspace(np.min(temp),np.max(temp),100)
    y = np.exp(intercept + (x  * slope))
    # plt.semilogy(x,y,linestyle='dashed',label = 'Regression line %s $Ea/R=%f$'%(str(i+8),slope))
    fuel_name = str(files[i]).split('_export.csv')[0] 
    plt.semilogy(temp,ID,marker='o',label = '$Fuel = %s ,P=5atm , X_{Fuel}=1, X_{Oxi}=Stochio, X_{Ar}=Rest$'%fuel_name)

    # plt.semilogy(x1,y1,linestyle='dashed',label = 'Regression line 1 $Ea/R=%f$'%slope1)

Ea_by_R['Fuel'] = pd.Series(fuel_list)
Ea_by_R['Ea/R'] = pd.Series(EaR_list)
Ea_by_R['intercept'] = pd.Series(intercepts_list)

Ea_by_R.to_csv('Ea_by_R.csv')




#plottinhg 
# plt.xlim(np.min(temp),np.max(temp))
# plt.ylim(np.min(ID),np.max(ID))
plt.rc('text',usetex=True)
plt.title('Ignition Delay Vs 1000/T')
plt.xlabel('1000/T')
plt.ylabel('Ignition Delay')
plt.legend(loc='best')
plt.savefig('./plots/combined.eps')
plt.show()
