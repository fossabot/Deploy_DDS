'''
Module checked works with any kind of tree

converting array in format that is compatible for printing
                1
        2               3
    4       5       6       7   
    8     9 10   11 12   13 14   15    

    which can be written as which also useful for latex tikZ,
    1
    2
        4
            8
            9
        5
            10
            11
    3
        6
            12
            13
        7
            14  
            15
by level oredering traversing ,
result will be : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
but to print in tikz(latex) in should be ,
result should be : 1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
by following pattern(9/(division_brach=2) = 4.5 < 5 ) it is implemented.
input : level order traversing array 
output : tikz compatible error
'''
import copy 
import time
import random
import string

tikz_array_modified = dict()


# #binary 
# for i in range(1,32):
#     key = i
#     value = random.choice(string.ascii_letters)
#     tikz_array_modified.update({key:value})
    
# key_index_array = [1,2,4,8,16]
# number_of_levels = len(key_index_array)-1
# type_of_division = 2

#tertiary 
for i in range(1,122):
    key = i
    value = random.choice(string.ascii_letters)
    tikz_array_modified.update({key:value})
    
key_index_array = [1,2,5,14,41]
number_of_levels = len(key_index_array)-1
type_of_division = 3


final_tikz_list = copy.deepcopy(key_index_array)
#copy from here 
# first elements appended
final_tikz_array = dict()
for i in range(number_of_levels+1):
    key = key_index_array[i]
    value = tikz_array_modified.get(key)
    final_tikz_array.update({key:value})

#using above initial label updating the 
def control_function(num,type_of_division):
    '''
    This method calculates control formula which is useful for traversing in the tree
    '''
    return num*type_of_division+1


def check_forward(control_value,control_index ,key_index_array,tikz_array_modified,tikz_array_required,upper_bound):
    '''
    A.
    THis method will append value till second last element
    starting with second last element--
    array : [1,2,5,14,41]
    map : [4,7,16,43,XX]  formula : 3^i+1

    increment till array values 41 -> 42 -> 43 -> 44

    as 44 of array  > 43 of map so, traverse back 

    control on 3rd element 
    1. if second last element print all child
    2. after printing go back till control value is greater function changed 
    go to B.

    C. traverse forward increment every element by one and also append in final list. Repeat till second last element.
    array : [1,2,5,15,44]
    map : [4,7,16,46,XX]

    as now second last element print all child and go to step A.

    '''
    print('control_value: ', control_value)
    while(control_index < len(key_index_array)-2):
        key_index_array[control_index+1] += 1
        print('key_index_array: ', key_index_array)
        key = key_index_array[control_index+1]
        print('key: ', key)
        value = tikz_array_modified[key]
        print('value: ', value)
        tikz_array_required.update({key:value})
        print('tikz_array_required: ', tikz_array_required)
        control_index += 1
    print('key_index_array: ', key_index_array)
    print('tikz_array_required: ', tikz_array_required)
    if(control_index == len(key_index_array)-2): #starts with 0 and 1 less so -2
        for i in range(type_of_division):
            key = key_index_array[control_index+1]
            print('key: ', key)
            value = tikz_array_modified[key]
            print('value: ', value)
            tikz_array_required.update({key:value})
            print('tikz_array_required: ', tikz_array_required)
            key_index_array[control_index+1] += 1
            print('key_index_array: ', key_index_array)
        #if upper bound reached return 
        if(key == upper_bound):
            return
    print('tikz_array_required: ', tikz_array_required)
    check_backward(control_value,control_index,key_index_array,tikz_array_modified,tikz_array_required,upper_bound)

def check_backward(control_value,control_index,key_index_array,tikz_array_modified,tikz_array_required,upper_bound):
    '''
    B.
    for tertiary,
    array : [1,2,5,14,44]
    map : [4,7,16,43,XX]

    43 < 44
    but 
    16 !< 14
    so, control on second 
    go to C.


    '''
    while(control_value <= key_index_array[control_index+1]):
        control_index -= 1
        print('control_index: ', control_index)
        control_value = control_function(key_index_array[control_index],type_of_division)
        print('control_value: ', control_value)
    print('control_index: ', control_index)
    print('control_value: ', control_value)
    print('key_index_array: ', key_index_array)
    check_forward(control_value,control_index,key_index_array,tikz_array_modified,tikz_array_required,upper_bound)
    #if upper bound reached return 
    if(key == upper_bound):
        return



#initial control to second-final element-1
tikz_array_required = dict()
control_index = number_of_levels-1

upper_bound = 0
for i in range(number_of_levels+1):
    upper_bound += type_of_division**i

print('upper_bound: ', upper_bound)

print('key_index_array: ', key_index_array)

for i in range(number_of_levels):
    key = key_index_array[i]
    value = tikz_array_modified.get(key)
    tikz_array_required.update({key:value})

while(key_index_array[control_index+1] < upper_bound):
    control_value = control_function(key_index_array[control_index],type_of_division) 
    check_forward(control_value,control_index ,key_index_array,tikz_array_modified,tikz_array_required,upper_bound)

tikz_array_required = list(tikz_array_required.keys())
print('tikz_array_required: ', tikz_array_required)
