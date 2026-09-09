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
student_info(name = "jana" , age = 20 , city = "sivaganga")"""      
    

def grocery_list(**grocery_product):
        for key,value in grocery_product.items():
            print(f"{key}:{value}")
grocery_list(tomato = "5kg" , carrot = "2kg", cucumber = "5pc")
