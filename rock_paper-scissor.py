"""
Game name:

Rock/Paper/Scissors

Creator: Husanjon Kamolov 

"""
import random as r

choices = ('r','p','s')
emojis = {'r':'🪨','p':'📜','s':'✄'}

while True:
      
      computer_choice = r.choice(choices)
      user_choice = input('Rock, paper, scissors? (r/p/s): ').lower()
      
      if user_choice not in choices:
        print('Invalid choice! ')
        continue
      
      print(f'You chose {emojis[user_choice]}')
      print(f'Computer chose {emojis[computer_choice]}')
      
    
      if (
          (computer_choice == 'r' and user_choice == 'p') or 
          (computer_choice == 'p' and user_choice == 's') or 
          (computer_choice == 's' and user_choice == 'r')):
        print('You win!')
      elif computer_choice == user_choice:
          print('Tie!')
      else:
        print('You lose!')
      
      repeat = input('Continue? (y/n): ').lower()
      if repeat == 'n':
        break

     
    

