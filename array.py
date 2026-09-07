"""from array import * 
arr1 = array('i', [33,44,55,6,3,4,56,7,67])
print(type(arr1))"""


"""from array import *
arr1 = array('f', [2.5, 4.8, -3.2, 6.7])

for i in arr1:
    print(i)
    if i < 0:
        print("negative number is not allowed")
        continue"""


import array
arr1 = array.array('i',[4,8,15,16,23])
total = sum(arr1)
print("The sum of the elements in the array is:", total)
    