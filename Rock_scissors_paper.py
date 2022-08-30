#Rock, paper, scissors, Project from the 100 Days of Code course, Teacher: Angela Li
# Student Lukasz Swiatek Brzezinski
#Despite of the program I add the improvements like:
#Add the while loop to this game, so you can play as many turns as you wish,
#You can show the scores and exit from the game.


import random

#figures for the game (modified from ASCII ART,
#originals: Rock=Fist - JW, Paper=Hand - DrS, Scissors=Hand - VK 

print("!!!Rock, paper, scissors GaMe!!!")

Rock = '''
       ,--.--._
------" _, \___)
 ROCK   / _/____)
        \//(____)
------\     (__)
       `-----"
 
'''

print(Rock)

Paper = '''

             ..__
  __..--""" ._ __.'
              "-..__
    PAPER    '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       
'''
print(Paper)

Scissors = '''
    .-.  _
    | | / )
    | |/ / SCISSORS
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

'''

print(Scissors)


Player = input("What is your name?") #Player name input
Choice_list = [Rock, Paper, Scissors]
Turn_No = 0
Computer_scores = 0
Human_scores = 0

while True:

    Action = int(input("What would you like to do: 1 - Play game, 2 - show the points, 3 - Exit"))
    if Action == 1:
        
        Computer_choice = random.choice(Choice_list) #computer choose it's figure

        Human_choice = input("Choose the figure from 1 to 3 you want to use: 1-Rock, 2-Paper, 3-Scissors").strip().capitalize()
        print()
        Human_figure = Choice_list[int(Human_choice)-1]

        # Figure chosen by Player and Computer displayed on the screen (code below):

        print("Computers figure:\n {0:s}\n {1:s} figure: \n {2:s}".format(Computer_choice,Player,Human_figure)) 

        #Winning or draw conditionals below:

        if Computer_choice == Human_figure:
            print('It\'s a draw')
            Computer_scores += 1
            Human_scores += 1
        elif (Computer_choice == Rock and Human_figure == Scissors) or (Computer_choice == Scissors and Human_figure == Paper):
            print("Computer's WIN this turn!!!")
            Computer_scores += 1
        else:
            print(f"{Player} WIN this turn!!!")
            Human_scores += 1

        Turn_No += 1
        
    elif Action == 2:
        print(f"Turn number: {Turn_No}, your scores: {Human_scores}, Computer scores: {Computer_scores}.")  

    elif Action ==3:
        print(f"Turn number: {Turn_No}, your scores: {Human_scores}, Computer scores: {Computer_scores}.")  
        if Human_scores > Computer_scores:
            print(f"CONGRATULATION!!! {Player} WIN THE GAME!!!")
        elif Human_scores < Computer_scores:
            print(f"{Player} loose the game. Congrats to me, your computer!!! Ha,Ha,Ha!!!")
        else:
            print("It's a DRAW!")
        print("Good bye!!!")
        break

