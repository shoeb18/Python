# write a program to print the multiplication table of a given number

num = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")