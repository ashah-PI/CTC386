# Arpita Shah
# Lab 2

a = int (input("How many bits binary do you want to convert into decimal "))
answer = 0

for i in range (a):
  digit = int(input ("Enter the digit with each prompt from most significant to less significant "))
  if (digit ==1):
    answer = answer + 2**(i)
  
  
print ("The number in decimal is ", answer) 
