# base class
class Employee:
    company = "Google"
    
    def show_details(self):
        print("This is an employee")
    

# derived class 
class Programmer (Employee):
    language = "Python"
    
    def get_language(self):
        print(f"The language is {self.language}")

    # method overriding
    def show_details(self):
        print("This is a programmer")
        

shoeb = Employee()
gaurav = Programmer()

shoeb.show_details()
gaurav.show_details()
    