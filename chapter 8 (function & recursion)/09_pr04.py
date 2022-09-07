# find the sum of n natural numbers using recursion

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
    
    
print("The sum of 1 to 10 is :",sum(10))