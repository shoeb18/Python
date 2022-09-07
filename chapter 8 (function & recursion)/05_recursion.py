# factorial using function
def fact_iter(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact
    

# factorial using recursion
def fact_recursion(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact_recursion(n-1)
    
    
num = int(input("Enter the number : "))

print(f"The factorial of {num} is :",fact_iter(num))
print(f"The factorial of {num} is :",fact_recursion(num))