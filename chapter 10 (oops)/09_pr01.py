# create a class programmer for storing information a few programmers working at microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def getInfo(self):
        print(f"The name of employee is {self.name}")
        print(f"The age of employee is {self.age}")
        print(f"The salary of employee is {self.salary}")
        

shoeb = Programmer("Shoeb",19,850000)
shoeb.getInfo()

        