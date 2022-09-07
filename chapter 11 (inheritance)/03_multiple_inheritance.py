# base class
class gamer:
    def get_gamer(self,name):
        print(f"Hi I'm {name} and I am a Gamer")

# base class
class programmer:
    def get_programmer(self,name):
        print(f"Hi I'm {name} and I am a Programmer")


# derived class
class gameDev (gamer,programmer):
    def get_gamedev(self,name):
        print(f"Hi I'm {name} and I am a Game Developer")
        
    
shoeb = gameDev()
shoeb.get_gamer("Shoeb")
shoeb.get_programmer("Shoeb")
shoeb.get_gamedev("Shoeb")
        