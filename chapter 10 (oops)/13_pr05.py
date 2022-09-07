class Train:
    
    def __init__(self,name ,fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def get_train_status(self):
        print(f"The name of the train is : {self.name}")
        print(f"The fare of the train is : {self.fare}")
        print(f"The seats of the train is : {self.seats}")
        
    def book_ticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked and your seat no. is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry! train is full try in tatkal")
            
    def cancel_ticket(self):
        pass
        
        
rajdhani = Train("Rajdhani Express 07",150,5)
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.get_train_status()