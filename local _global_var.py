"""a = 10

def nothing():
 x = 15
 print("inside variable : ",x )
nothing()

print("outside variable :" , a)

 
def add_numbers():
    x = 3
    y = 4
    result = x + y
    print(result)
add_numbers() 
print(result)"""

balance = 1000

def withdraw(amount):
    global balance
    balance = balance - amount
    print(balance)
withdraw(200)
print(balance)     

