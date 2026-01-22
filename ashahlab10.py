# Arpita Shah
# Lab 10

import math

# This is for my function definitions
def temp_convrt():
  y = int(input("Enter the number in Fahrenheit to convert in to Celsius."))
  c = (y-32)* (5/9)
  print( y, "degree Fahrenheit = ", c, "degree Celsius")

def qudratic_function():
  ans1 = 0
  ans2 = 0
  print("Enter the value of a, b and c from f(x) = ax^2+bx+c")
  a = float(input("Enter the value of a "))
  b = float(input(" Enter the value of b "))
  c = float(input("Enter the value of c "))
  print (" ** Vertex is (" , (-b)/(2*a) , ",", a*(-b/(2*a))**2 + b*(-b)/(2*a) + c ,") **")
  if (a > 0):
      print ("** Parabola opens up **")
  else:
      print ("** Parabola opens down **")
  if (b*b - 4 *a*c <0):
    print("**No real solution exit**")
    print ("**y intercept is (0, " , c ,")**")
    
  else: 
    ans1 = (-b + math.sqrt(b*b - 4 *a*c))/(2*a)
    ans2 = (-b - math.sqrt(b*b - 4 *a*c))/(2*a)
    print("** x intercepts are (", ans1 , ", 0) and (", ans2, ", 0) **")
    print ("** y intercept is (0, " , c ,") **")
  print ("*******************************************************")  

# This is the main section
name= input("Enter your name: ")
print ("-------------------------------------------------")
print ("Option 1: Joke")
print ("Option 2: Your name")
print ("Option 3: Famous Quote")
print ("Option 4: Guessing Game")
print ("Option 5: Convert input Fahrenheit in to Celsius")
print ("Option 6: Finding Characteristic of Quadratic Function(s) ")
print ("-------------------------------------------------")

x = 102
#guess = 67
option = int(input ("Enter the option number that you would like to pick "))
if (option ==1):
  print ("What comes after USA? --------- USB")
if (option ==2):
  for i in range (15):
     print(name)
     
if (option ==3):
  print("Hello", name)
  number= int(input("Enter the number to choose option 3: "))
  for i in range (number):
    print("You miss 100 percent of the shots you never take.")
    
if (option == 4):
  x = 102
  while (x<0 or x>100):
   while(x!=67):
      x = int(input("Enter the number that I am guessing between 0 to 100 inclusive. "))
  if (x>100 or x<0):
       print("Your number wasn't in the range. Enter the number between 0 to 100 inclusive.")
  else:
       if (x> 67):
          print("Number is larger compare to the guessed number. Let's try again! ")
       if (x< 67):
        print ("Number is smaller compare to guessed number.  Let's try again! ")
       if (x == 67):
          print("You guess the number ", x , "correctly. You are amazing!")

if (option ==5):
  temp_convrt()
  
if (option ==6):
  print ("You will be able to find the various characteristic of parabola ")
  question = int(input("How many problems do you want to solve?"))
  for i in range (question):
    qudratic_function()
  
