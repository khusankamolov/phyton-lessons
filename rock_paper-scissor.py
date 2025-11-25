"""
Game name:

Rock/Paper/Scissors

Creator: Husanjon Kamolov 

"""
import random as r

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK:'🪨',PAPER:'📜',SCISSORS:'✄'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
      user_choice = input('Rock, paper, scissors? (r/p/s): ').lower()
      
      if user_choice in choices:
          return user_choice
      else:
        print('Invalid choice! ')
        continue
    
def display_choices(user_choice,computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def get_winner(user_choice,computer_choice):
    if (
        (computer_choice == ROCK and user_choice == PAPER) or 
        (computer_choice == PAPER and user_choice == SCISSORS) or 
        (computer_choice == SCISSORS and user_choice == ROCK)):
      print('You win!')
    elif computer_choice == user_choice:
        print('Tie!')
    else:
      print('You lose!')
      
def play_game():
    
  while True:
      
     user_choice = get_user_choice()
     computer_choice = r.choice(choices)
    
     display_choices(user_choice,computer_choice)

     get_winner(user_choice,computer_choice)
      
     repeat = input('Continue? (y/n): ').lower()
     if repeat == 'n':
      break
  
play_game()

     
    

