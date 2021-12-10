from gamecomponents import gamevar
import random 
guess = ""
answer = random.choice(gamevar.list1)
gamevar.playerLives = 4 
print("==========================================================================")
print("Welcome to the super-hero guessing game! Lets start with our first quetion")
print("==========================================================================")
lose = False


while gamevar.playerLives != 0 :
    quetionSpider = random.choice(gamevar.listspider)
    quetioniron = random.choice(gamevar.listiron)
    quetioncap = random.choice(gamevar.listcap)
    if answer == "Spider-Man" :
 
            print(quetionSpider)
            print("==========================================================================")
            gamevar.player = input("Can you guess who you are ? ")
           

    if answer == "Iron-Man" :

        print(quetioniron)
        print("==========================================================================")
        gamevar.player = input("Can you guess who you are ?  ")
    

    if answer == "Captin-America" :
    
        print(quetioncap)
        print("==========================================================================")
        gamevar.player = input("Can you guess who you are ? ")
     

    if gamevar.player == answer :
        gamevar.playerLives = 0
        print("You get it ! It is "+ answer)
    elif  gamevar.player != answer :
        print("unlucky ! lets try again ")
        gamevar.playerLives = gamevar.playerLives - 1
    elif gamevar.playerLives == 0: print("Out of guessing chance, You Lose") 

