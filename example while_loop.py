##beginner##

"""count = 1
while count <= 5:
    print(count)
    count = count + 1"""


"""n = int(input("Enter an age: "))
while n<0:
    print( "invalid age" , n)
    n = int(input("Enter an age: "))
    print("current age is", n)"""    


##intermediate##

"""while True:
    n = int(input("Enter a number: "))
    if n == 0:
        print("You entered 0, exiting the loop.")
        break
    print("You entered:", n)"""



"""num = 12345
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print("The sum of the digits is:", total)""" 


##advanced##

attempts = 0
while attempts < 3:
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted.")
        break
    else:
        attempts += 1
        print("Incorrect password. Attempts left:", 3 - attempts)






