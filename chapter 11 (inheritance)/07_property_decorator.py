class Employee:
    company = "Hp"
    salary = 1000
    salary_bonus = 500
    # total_salary = 1500

    # property work as method (getter method)
    @property
    def total_salary(self):
        return self.salary + self.salary_bonus
    
    @total_salary.setter
    def total_salary(self,val):
        self.salary_bonus = val - self.salary

shoeb = Employee()
print(shoeb.total_salary)

shoeb.total_salary = 1800
print(shoeb.salary)
print(shoeb.salary_bonus)