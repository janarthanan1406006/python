"""from array import *
arr1 = array('i', [20,3,9,900,76,87,45])
arr1.append(25)
print(arr1)

from array import *
arr1 = array('i', [20,3,9,900,76,87,45])
result = arr1.count(76)
print(result)



from array import *
arr1 = array('i', [20,3,9,900,76,87,45])
arr1.reverse()
print(arr1)"""



from array import *
arr1 = array('i', [20,3,9,900,76,87,45])
arr1.insert(2, 800)
arr1.remove(9)
result = arr1.index(76)
arr1.extend([100,200,300])
print(arr1)
print(result)