import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import os
import random

data = pd.read_csv('tranformed_data.csv')
data = data.drop(columns=['Constant','Time'])
# obtain svd
U, S, V = np.linalg.svd(data)

# inspect shapes of the matrices
print(U.shape, S.shape, V.shape)

print(S)

#link:https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60


def pca_analysis(data,compo):
    #PCA
    pca = PCA(n_components=compo)
    principalComponents = pca.fit_transform(data)
    return principalComponents, pca

#1d
D1_data, pca = pca_analysis(data,1)
principalDf = pd.DataFrame(data = D1_data, columns = ['principal component 1'])

#variance
explained_variance = pca.explained_variance_ratio_
print('explained_variance: ', explained_variance)

#plotting
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_title('1 component PCA', fontsize = 20)
ax.scatter(principalDf['principal component 1'],np.zeros(principalDf.shape[0]))
ax.legend()
ax.grid()   
plt.show()

#2d
D2_data, pca = pca_analysis(data,2)
principalDf = pd.DataFrame(data = D2_data
             , columns = ['principal component 1', 'principal component 2'])

#variance
explained_variance = pca.explained_variance_ratio_
print('explained_variance: ', explained_variance)

#plotting
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
ax.scatter(principalDf['principal component 1']
               , principalDf['principal component 2'])
ax.legend()
ax.grid()   
plt.show()


#3d
D2_data, pca = pca_analysis(data,3)
principalDf = pd.DataFrame(data = D2_data
             , columns = ['principal component 1', 'principal component 2', 'principal component 3'])

#variance
explained_variance = pca.explained_variance_ratio_
print('explained_variance: ', explained_variance)

#plotting
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_zlabel('Principal Component 3', fontsize = 15)
ax.set_title('3 component PCA', fontsize = 20)
ax.scatter(principalDf['principal component 1']
               , principalDf['principal component 2'],principalDf['principal component 3'])
ax.legend()
ax.grid() 
plt.savefig('3d.eps')  
plt.show()
plt.close()
plt.clf()


#2d
#Reading final files
files =  os.listdir('./result/final_cluster_result/')
for i in files:
    color = "#%06x" % random.randint(0, 0xFFFFFF)
    data = pd.read_csv('./result/final_cluster_result/'+str(i))
    data = data.drop(columns=['Constant'])
    data = data.drop(columns=['y_act'])
    data = data.drop(columns=['y_pred'])

    D2_data, pca = pca_analysis(data,2)
    principalDf = pd.DataFrame(data = D2_data
             , columns = ['principal component 1', 'principal component 2'])


    #variance
    explained_variance = pca.explained_variance_ratio_
    print('explained_variance: ', explained_variance)

    #plotting
    plt.xlabel('Principal Component 1', fontsize = 15)
    plt.ylabel('Principal Component 2', fontsize = 15)
    plt.title('2 component PCA', fontsize = 20)
    plt.scatter(principalDf['principal component 1'], principalDf['principal component 2'],c=color)
    plt.legend()
    plt.grid()   

plt.show()



plt.close()
plt.clf()


#3d
#Reading final files
files =  os.listdir('./result/final_cluster_result/')
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_ylabel('Principal Component 3', fontsize = 15)
ax.set_title('3 component PCA', fontsize = 20)
ax.legend()
ax.grid() 
for i in files:
    color = "#%06x" % random.randint(0, 0xFFFFFF)
    data = pd.read_csv('./result/final_cluster_result/'+str(i))
    data = data.drop(columns=['Constant'])
    data = data.drop(columns=['y_act'])
    data = data.drop(columns=['y_pred'])

    D2_data, pca = pca_analysis(data,3)
    principalDf = pd.DataFrame(data = D2_data
             , columns = ['principal component 1', 'principal component 2','principal component 3'])


    #variance
    explained_variance = pca.explained_variance_ratio_
    print('explained_variance: ', explained_variance)

    #plotting
    ax.scatter(principalDf['principal component 1'], principalDf['principal component 2'],principalDf['principal component 3'])

  
plt.show() 