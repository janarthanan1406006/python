"""fruits = ["apple", "banana", "cherry"]
for y in fruits:
    print(y)"""



"""for x in range(15):
    print(x)"""


## intermediate problem ##

"""num = [1,2,3,4,5,6,7,8,]
for x in num:

    if x % 2 == 0:
        print("even number", x)"""



## advanced ##

"""for i in range(2,50):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)"""    


for i in range(2,50):
    for j in range(2,i):
        if i % j == 0:
            print("composite number", i)
            break
            