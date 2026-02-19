# Arpita Shah
# Lab 2

bit1 = int(input( "Enter your first bit binary (from most to less significant digit to convert as decimal  "))
bit2 = int(input( "Enter your second bit binary to convert as decimal  "))
bit3 = int(input( "Enter your third bit binary to convert as decimal  "))
bit4 = int(input( "Enter your third bit binary to convert as decimal  "))
bit5 = int(input( "Enter your third bit binary to convert as decimal  "))
bit6 = int(input( "Enter your third bit binary to convert as decimal  "))

answer = 0

if (bit1 == 1 ):
 answer = 1

if (bit2 == 1):
  answer = answer + 2

if (bit3 == 1):
  answer = answer + 4
  
if (bit4 == 1):
  answer = answer + 2**3
  
if (bit5 == 1):
  answer = answer + 2**4
  
if (bit6 == 1):
  answer = answer + 2**5  
  
print("The decimal value is ", answer) 
 
