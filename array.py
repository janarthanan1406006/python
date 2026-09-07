"""from array import * 
arr1 = array('i', [33,44,55,6,3,4,56,7,67])
print(type(arr1))"""


from array import *
arr1 = array('f', [2.5, 4.8, -3.2, 6.7])

for i in arr1:
    print(i)
    if i < 0:
        print("negative number is not allowed")
        continue