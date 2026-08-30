"""def grade(score):
    match score:
        case score if score >= 90:
            print(" a score ")
        case score if score >= 80:
            print(" b score")
        case score if score >= 70:
            print(" c score")
        case _:
            print(" fail ")        
grade(85)"""



"""def color(rgb):
    match rgb:
        case (255 ,0 , 0 ):
            print("red")
        case (0 , 0, 0):
            print("black")
        case (255 , 255 , 255):
            print("white")
        case (10, 20, 30):
            print("dark blue")    
        case _:
            print("unknown color")

color((0,10,20))"""



def calculator(calc):
    match calc:
        case {"op": "add", "a": a, "b": b}:
            print(a +b)
        case {"op": "sub", "a": a, "b": b}:
            print(a - b)
        case {"op": "mul", "a": a, "b": b}:
            print(a * b)
        case {"op": "div", "a": a, "b": b} if b== 0:
            print("division by zero is not allowed")
        case {"op": "div", "a": a, "b": b} if b!= 0:
            print(a / b)    
        case {"op": "mod", "a": a, "b": b}:
            print(a % b)
        case _:
            print("invalid operation")
calculator({"op": "div", "a": 10, "b": 0})
calculator({"op": "div", "a": 10, "b": 2})
calculator({"op": "mod", "a": 10, "b": 3})
         
