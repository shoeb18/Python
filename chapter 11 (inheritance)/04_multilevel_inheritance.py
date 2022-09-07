# base class
class baby:
    def baby_info(self,name):
        print("My name is",name)
        print("I am a baby.")
        print("My age is 3.")

# derived class for baby
class boy (baby):
    def boy_info(self,name):
        print("My name is",name)
        print("I am a boy.")
        print("My age is 19.")

# derived class for boy
class men (boy):
    def men_info(self,name):
        print("My name is",name)
        print("I am a men.")
        print("My age is 25.")
        

shoeb = men()
shoeb.baby_info("Shoeb")
shoeb.boy_info("Shoeb")
shoeb.men_info("Shoeb")