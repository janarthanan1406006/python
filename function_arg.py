#default argument

"""def hello (name, text = " welcome to python"):
    print(f"{name},{text}")
hello("jana")
hello("asha" , "welcome to vs code")   

#variable length parameter

def add(*scores):
    print(scores)
    print(sum(scores))
add (80,65,43,67,56)
add(50,54,76)


def add(*names):
    print(names)
add ("asha","jana","vetri","santhosh")"""


#keyword arguments

"""def student_info(**student_details):
    for key,value in student_details.items():
        print(f"{key}:{value}")
student_info(name = "jana" , age = 20 , city = "sivaganga")     
    

def grocery_list(**grocery_product):
        for key,value in grocery_product.items():
            print(f"{key}:{value}")
grocery_list(tomato = "5kg" , carrot = "2kg", cucumber = "5pc")



#positional argument

def positional_argument(animal_type , pet_name):
    print(f"i have a {animal_type} named {pet_name}.")
positional_argument("dog" , "rocky")


def power_calculation(base , exponent = 2):
     print(base ** exponent)
power_calculation(5) 
power_calculation(2 ,3 )""" 


numbers = [10,20,30,40]

largest = numbers[0]

index = 0
while index < len(numbers):
    if numbers[index] > largest:
        largest = numbers[index]
    index += 1
print(f"the largest numbers: " , largest  )        
 
  