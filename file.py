# st="Hey I am Supercool"
# f=open("myfile.txt","w")
# f.write(st)
# f.close()

# with open("poems.txt","w") as f:
#     t=f.write("twinkle twinkle little star \n how i wonder what you are \n up above the world so high \n like a diamond in the sky")
#     if("twinkle" in t ):
#         print("got it")
#     else:
#         print("No")

import random
def game():
    print("You are playing the game: ")
    score= random.randint(1,100)
    with open("hiscore.txt") as t:
        hiscore= t.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score: {score}")
    if(score>hiscore or hiscore==""):
        with open("hitext.txt","w") as t:
            t.write(str(score))
            


    return score
game()