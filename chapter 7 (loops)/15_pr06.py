# write a program to find the factorial of a number

n = int(input("Enter the number : "))

i = 1
fact = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("The factorial of",n,"is :",fact)