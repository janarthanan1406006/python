"""for i in range(1,10):
    if i % 3 == 0:
        continue
    print(i)"""




"""for x in range(1, 20):
    if x == 14:
        break
    print(x)"""



"""correct_password = "xxx"
for attempt in range(3):
    password = input("enter the password: ")
    if password == correct_password:
        print("acces granted")
        break
    else:
        print("incorrect pasword, tryagain")""" 


"""number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in number:
    if x % 2 == 0:
        print(" first even number", x)
        break"""



num = 17
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

    

