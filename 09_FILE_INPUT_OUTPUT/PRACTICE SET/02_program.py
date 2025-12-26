# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.


import random 

def game():
    print("you are playing game...")
    score = random.randint(1,50)

    #fetch the highscore 
    with open("Hi-score.txt") as f:
        x = f.read()

        if x != "":
            x = int(x)
        else:
            x = 0

    print(f"You score :{score}")
    if(x < score):

        #write this hiscore to the file
        with open("Hi-score.txt","w")as f:
            f.write(str(score))
    
    return score

game()