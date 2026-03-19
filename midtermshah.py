#Arpita Shah
x = 20
x = int(input("Enter the number that I am guessing between 0 to 10 inclusive. "))
if (x>10 or x<0):
  print("Your number wasn't in the range. Enter the number between 0 to 10 inclusive.")
else:
  if (x!=7):
   print("Number that you guessed is ", x , "not the number I was thinking.")
  if (x == 7):
   print("You guess the number ", x , "correctly. You are amazing!")

