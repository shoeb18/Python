class Employee:
    
    salary = 1000
    increment = 1.5
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment