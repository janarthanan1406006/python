"""for i in range(1,10):
    if i % 3 == 0:
        continue
    print(i)"""




"""for x in range(1, 20):
    if x == 14:
        break
    print(x)"""



correct_password = "xxx"
for attempt in range(3):
    password = input("enter the password: ")
    if password == correct_password:
        print("acces granted")
        break
    else:
        print("incorrect pasword, tryagain") 



