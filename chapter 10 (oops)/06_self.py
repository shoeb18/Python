class Employee:
    
    company = "Google"

    def getSalary(self):
        print(f"Employee working in {self.company}")
        print(f"Salary is {self.salary}")

shoeb = Employee()

# both are same
# Employee.getSalary(shoeb)
# shoeb.getSalary()

shoeb.salary = 100000
shoeb.company = "Ubisoft"
shoeb.getSalary()