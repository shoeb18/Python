import random

def play_game(user):
    # random number generator
    rand_num = random.randint(1,3)
    # comp input
    if rand_num == 1:
        comp = 's'
    elif rand_num == 2:
        comp = 'w'
    else:
        comp = 'g'

    # choices
    print("you chose :",user)
    print("comp chose :",comp)

    # game starts here
    if user == comp:
        return None
    elif user == 's' and comp == 'w':
        return True
    elif user == 'w' and comp == 'g':
        return True
    elif user == 'g' and comp == 's':
        return True
    else:
        return False
        

# play game code
print("* * * __ Welcome to snake - water - gun __ * * *")
print("***_ s for snake")
print("***_ w for water")
print("***_ g for gun")

userInput = input("Enter your choice : ")
isWin = play_game(userInput)


if (isWin is None):
    print("Match is tie!")
elif (isWin):
    print("You win!")
else:
    print("You lose!")


