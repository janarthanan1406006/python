##beginner##

"""count = 1
while count <= 5:
    print(count)
    count = count + 1"""


n = int(input("Enter an age: "))
while n<0:
    print( "invalid age" , n)
    n = int(input("Enter an age: "))
    print("current age is", n)    
