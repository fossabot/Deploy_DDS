import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as spt
butane = 'butane'
decane_sarthy = 'decane_sarthy'
dodecane = 'dodecane'
dodecane_sarthy = 'dodecane_sarthy'
Heptane_sarthy = 'Heptane_sarthy'
Hexane = 'Hexane'
Nonane_sarthy = 'Nonane_sarthy'
octane_sarthy = 'octane_sarthy'
pentane = 'pentane'
propane = 'propane'
undocane_sarthy = 'undocane_sarthy'

folder_list = [butane,decane_sarthy,dodecane,dodecane_sarthy,Heptane_sarthy,Nonane_sarthy,octane_sarthy,pentane,]



def temp_ID(foldername1):
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


for i in range(len(folder_list)):
    ID , temp = temp_ID(folder_list[i])
    plt.semilogy(temp,ID,marker='o',label = '$Fuel = %s ,P=1.2atm , X_{Fuel}=0.4, X_{Oxi}=0.8, X_{Ar}=90.8$'%folder_list[i])




# #7 and 5 th point diffn

# #regression
# slope1, intercept1, r_value1, p_value1, std_err1 = spt.linregress(temp1,np.log(ID1))
# print('std_err1: ', std_err1)
# print('p_value1: ', p_value1)
# print('r_value1: ', r_value1)
# print('intercept1: ', intercept1)
# print('slope1: ', slope1)



# x1 = np.linspace(np.min(temp1),np.max(temp1),100)
# y1 = np.exp(intercept1 + (x1  * slope1))



#plottinhg 

# plt.semilogy(x1,y1,linestyle='dashed',label = 'Regression line 1 $Ea/R=%f$'%slope1)

# plt.xlim(np.min(temp),np.max(temp))
# plt.ylim(np.min(ID),np.max(ID))
plt.rc('text',usetex=True)
plt.title('Ignition Delay Vs 1000/T')
plt.xlabel('1000/T')
plt.ylabel('Ignition Delay')
plt.legend(loc='best')
plt.savefig('./plots/combined.png')
plt.show()
