# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 11:33:15 2025

@author: Surface
"""

import random as r
from uzwords import words 
def get_word():
        word=r.choice(words)
        while '-' in word or ' ' in word or "'" in word:
            word=r.choice(words)
        return word.upper() 


def display(user_letters,word):
    display_letters=""
    for letter in word:
        if letter in user_letters:
            display_letters+=letter
        else:
            display_letters+='-'
    return display_letters
            
def play():
    word=get_word()
    word_letters=set(word)
    user_letters=''
    print(f"\nI think a word with {len(word)} letters.Can you find it?")
    while word_letters:
         print(display(user_letters,word))
         if user_letters:
              print(f"\nYou used these words since beginning: {user_letters} ")            
               
         letter=input("\nEnter a letter:").upper()
         if letter in user_letters:
            print("Before, you entered this letter.")
            continue
         elif letter in word:
             word_letters.remove(letter)
             print(f'{letter} is right!')
         else:
            print(f'{letter} is wrong!') 
         user_letters+=letter
    print(f"Congrats,you can find {word.upper()} with {len(user_letters)} guesses.")
    return word
         
        
        
        


       
            
            
            
        
        
    

            


        