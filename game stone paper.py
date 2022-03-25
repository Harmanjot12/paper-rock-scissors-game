#Here computer is player1 you are player2

import random #random import to choose random option

def main():
    
    #control loop with 'y' variable 
    play_again = 'y' 

    while play_again == 'y':
        print('Lets play the game of paper, rock, scissors!') 
        print('Please choose the correct option') 
        
        #get method is used to get the player and computer opition
        computer_choice = get_computer_choice() 
        player_choice = get_player_choice() 

        #print the choices 
        print('Computer chosed : ', computer_choice) 
        print('You chosed : ', player_choice)
        
        
        #declare winner
        winner_result(computer_choice, player_choice)
        
        
        
        #ask the user if they want to play again 
        play_again = input("Play again? (y/n) : ")
        



#function for computer choice
def get_computer_choice(): 

    #use random function from library 
    choice = random.randint(1,3) #used to choose one random option as a player1

    if choice == 1:    
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS' 

    


#function for player choice
def get_player_choice():
    
    #choose one option from the above 
    choice = int(input("Select one from the above :- \nRock(1) \nPaper(2) \nScissors(3) \n "))
    
    #if entry number is invalid
    while choice != 1 and choice != 2 and choice != 3: 
        print('Please choose valid option') 
        choice = int(input('Select one from the above :- \nRock(1) \nPaper(2) \nScissors(3) \n  ')) 

    #applying conditional  statement 
    if choice == 1: 
        choice = 'ROCK' 
    elif choice == 2: 
        choice = 'PAPER' 
    else: 
        choice = 'SCISSORS' 

    #return value 
    return choice 
    


#function for declaring winner
def winner_result(computer_choice, player_choice): 

    #if its a tie 
    if computer_choice == player_choice:
        result = 'tie'
        print("Its a Tie")

    #conditions when you can win
    elif computer_choice == 'SCISSORS' and player_choice == 'ROCK':
        result = 'win'
        print('ROCK crushes SCISSORS! You win!')
    elif computer_choice == 'PAPER' and player_choice == 'SCISSORS': 
        result = 'win'
        print('SCISSORS cut PAPER! You win!')
    elif computer_choice == 'ROCK' and player_choice == 'PAPER': 
        result = 'win'
        print('PAPER covers ROCK! You win!')

    #if you loose
    else: 
        result = 'lose'
        print('You lose!')

main()
    
