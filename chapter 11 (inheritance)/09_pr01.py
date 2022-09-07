# create a class that represents 2d vector and 3d vector

class vector2:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

class vector3:
    
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.y = y
        
        
vec2 = vector2(4,5)
vec3 = vector3(3,5,6)

