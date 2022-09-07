class Employee:
    company = "Hyper-X"
    salary = 8000
    location = "Delhi"
    
    # def change_salary(self,salary):
    #     self.__class__.salary = salary
    
    # it gives your direct access to the class attributes
    @classmethod
    def change_salary(cls,salary):
        cls.salary = salary



shoeb = Employee()

print(shoeb.salary)
print(Employee.salary)

shoeb.change_salary(100)

print(shoeb.salary)
print(Employee.salary)