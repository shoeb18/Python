# base class
class baby:
    def baby_info(self,name):
        print("My name is",name)
        print("I am a baby.")
        print("My age is 3.")
        print("**************\n")

# derived class for baby
class boy (baby):
    def boy_info(self,name):
        print("My name is",name)
        print("I am a boy.")
        print("My age is 19.")
        print("**************\n")

# derived class for boy
class men (boy):
    def men_info(self,name):
        
        # super use for call its base class method or constructor
        super().baby_info("Shoeb")

        print("My name is",name)
        print("I am a men.")
        print("My age is 25.")
        print("**************\n")
        

shoeb = men()
shoeb.baby_info("Shoeb")
shoeb.boy_info("Shoeb")
shoeb.men_info("Shoeb")