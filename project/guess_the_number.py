import random

# random number generator
def gen_rand_num():
    rand_num = random.randint(1,100)
    return rand_num

# main game
def play_game():
    rand_num = gen_rand_num()
    guesses = 1
    user_input = None
    
    while(user_input!=rand_num):
        user_input = int(input("Enter your guess : "))

        if (user_input == rand_num):
            print("You guessed it right! You guessed it in",guesses,"attempts")
        elif (user_input < rand_num):
            print("Enter higher value")
        else:
            print("Enter lower value")
        guesses+=1
        
        
# play game
play_game()
    
    