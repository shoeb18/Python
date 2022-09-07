# print following pattern
# ***
# **
# *

def Pattern(n):
    for i in range(n):
        print("*" * (n-i))
        
Pattern(5)