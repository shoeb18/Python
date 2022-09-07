# write a program to find the given user input number is prime or not

num = int(input("Enter the number : "))
is_prime = True

for i in range(2,num):
    if (num%i==0):
        is_prime = False
        break

if (is_prime):
    print(num,"is prime")
else:
    print(num,"is not a prime")
        