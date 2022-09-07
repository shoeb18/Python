# write a program to convert celsius into fahrenheit

def cel_to_fahr(cel):
    return (cel * 1.8)+32

celsius = int(input("Enter the celsius value : "))

print(f"The value of {celsius} celsius in fahrenheit is :",cel_to_fahr(celsius))