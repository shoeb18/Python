# write a function to print the multiplication table of n

def multi_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
        
        
multi_table(5)