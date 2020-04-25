import numpy as np
file_name = []
label = ['e','c','a','d','b']
sorted_by_reg_error = ['a','b','c','d','e']
cluster_label = []

i = 0
while(i != len(sorted_by_reg_error)):
    j = 0
    while(True):
        if(sorted_by_reg_error[i] == label[j]):
            #appending
            cluster_label.append(label[j])
            #deleting
            label.pop(j)
            i += 1
            break
        j += 1
print('cluster_label: ', cluster_label)