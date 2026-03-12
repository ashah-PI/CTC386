#Arpita Shah
#Finding the sum of finite arithmetic series.
sn=0
an=0
print("Let's find the sum of finite arithmetic series")
a=int(input("Enter the value of the first term  "))
n = int(input("How many terms do you want to add?  "))
d= int(input("What is the difference between two terms  "))
an= a +(n-1)*d
sn=n*(a+an)/2
print("The sum of first ",n, " terms equal to ",sn)
