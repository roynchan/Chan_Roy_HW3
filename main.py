from gamecomponents import gamevar
import random 
guess = ""
answer = random.choice(gamevar.list1)
print(answer)
quetionSpider = random.choice(gamevar.listspider)
quetioniron = random.choice(gamevar.listiron)
quetioncap = random.choice(gamevar.listcap)
lose = False
while gamevar.player == False and gamevar.playerLives > 0 :
    if answer == "Spider-Man" :
            print(quetionSpider)
            gamevar.player = input("Enter Your Guess! ")
           

    if answer == "Iron-Man" :
        print(quetioniron)
        gamevar.player = input("Enter Your Guess! ")
    

    if answer == "Captin-America" :
        print(quetioncap)
        gamevar.player = input("Enter Your Guess! ")
     

    if gamevar.player == answer :
        gamevar.player = True
        print("You get it ! It is"+ answer)
    elif  gamevar.player != answer :
        print("unlucky ! lets try again ")
        gamevar.playerLives = gamevar.playerLives - 1
    else : print("Out of guessing chance, You Lose")

