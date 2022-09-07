# class attributes are linked with class

class Employee:
    company = "Google"


shoeb = Employee()

print(shoeb.company)
Employee.company = "Youtube"
print(shoeb.company)
