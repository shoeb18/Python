class calculator:
    def __init__(self,num):
        self.number = num
        
    def square(self):
        print("The value of square is :",self.number**2)
        
    def square_root(self):
        print("The value of square root is :",self.number**0.5)
    
    def cube(self):
        print("The value of cube is :",self.number**3)
        
    @staticmethod
    def greet():
        print("*** Hello welcome to the best calculator of the world ***")


num = calculator(9)
num.square()
num.square_root()
num.cube()
num.greet()