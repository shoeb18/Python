def game():
    return 55

score = game()

with open("highscore.txt") as f:
    hiscore = int(f.read())
    
if hiscore < score:
    with open("highscore.txt",'w') as f:
        f.write(str(score))
    

