# find the greatest number of 4 numbers entered by the user
n1 = int(input("Enter the number 1 : "))
n2 = int(input("Enter the number 2 : "))
n3 = int(input("Enter the number 3 : "))
n4 = int(input("Enter the number 4 : "))

f1 = 0
f2 = 0

# comparing n1 and n2
if (n1>n2):
    f1 = n1
else:
    f1 = n2

# comparing n3 and n4
if (n3>n4):
    f2 = n3
else:
    f2 = n4

# comparing f1 and f2
if (f1>f2):
    print(f1,"is greater")
else:
    print(f2,"is greater")