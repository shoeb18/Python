class Employee:
    
    # static method is run without self
    @staticmethod
    def greet():
        print("Good morning sir")

shoeb = Employee()
shoeb.greet()