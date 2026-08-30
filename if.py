##num = 15
##if num > 0:
  ##  print("positive number")
##elif num < 0:
  ##  print("negative number")
##else:
  ##  print("zero")       





##age = 16

##if age >= 18:
    ##print("allowed to watch the 18+ movie")
##else:
    ##print("not allowed to watch 18+ movie") 


mark = 82
if mark >= 90:
    print(" a grade")
elif mark >= 75 and mark <= 89:
    print(" b grade")
elif mark >= 50 and mark <=74:
    print(" c grade ")
else:
    print(" fail ")  



##num = int (input(" enter the number: "))
##if num < 0:
  ##  print(" positive number ")
##elif num > 0:
  ##  print(" negative number ")
##else:
  ##  print(" zero ")   




##num = int (input(" enter the number: "))
##if num < 0:
  ##  print(" negative number ")
##elif num > 0:
  ##  print(" positive number ")
##else:
  ##  print(" zero ") 



num1 = 3
num2 = 5
operator = input("enter the operator: ")
if operator == "addition":
    print("addition is successful" , num1 + num2)
elif operator == "subtraction":
    print("subtraction is successful" , num1 - num2)
elif operator == "multiplication":
   print("multiplication is successful" , num1 * num2)
elif operator == "division":
   print("division is successful" , num1 // num2)
else:
  ##2  print(" invalid operator ")




sides1 = int (input("enter the sides of the triangle1: "))
sides2 = int (input("enter the sides of the triangle2: "))
sides3 = int (input("enter the sides of the triangle3: "))

if sides1 == sides2 == sides3:
    print(" it is equalateral triangle")
elif sides1 == sides2:
    print(" it is isosceles triangle")    

else:
    print("scalene triangle")           