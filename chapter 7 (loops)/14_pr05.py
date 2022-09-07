# write a program to sum of first n natural numbers using while loop

num = int(input("Enter the number : "))

i = 0
sum = 0

while i<=num:
    sum = sum + i
    i = i + 1

print("The sum from 1 to",num,"is :",sum)