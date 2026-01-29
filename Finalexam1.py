# Arpita Shah
# Fianl Exam example 1
print ("-------------------------------------------------")
print ("Option 1: Joke")
print ("Option 2: Display the name of the food 20 times")
print ("Option 3: Enter the number that I am thinking.")
print ("-------------------------------------------------")

option = int(input ("Enter the option number that you would like to pick "))

if (option ==1):
  name= input("Enter your name: ")
  print (name, ":  Why is 6 aftraid of 7; because 7 8 9!")
if (option ==2):
  for i in range (20):
     print("Fajita")
if (option ==3):
  
  x = 5
  
  while(x!=0):
    x = int(input("Enter the number that I am thinking. "))

    if (x> 0):
      print("That is not the number I am thinking. Let's try again! ")
       
    if (x == 0):
      print("You guess the number ", x , "correctly. You are amazing!")
   
