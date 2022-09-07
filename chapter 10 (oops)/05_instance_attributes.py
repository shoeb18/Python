# class attributes are linked with class

class Employee:
    company = "Google"
    salary = 100000

shoeb = Employee()

# instance attribute take first preference than class attribute

shoeb.salary = 5000
print(shoeb.salary)

# if attribute it doesn't present then it use class attributes
# or both not present then throws an error  
print(shoeb.address)
