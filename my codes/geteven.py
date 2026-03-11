# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 15:11:42 2025

@author: Surface
"""

numbers=[12,13,34,22,55,43,54,66,72,32,34,68]

def get_even(numbers=numbers):
    """This function returns only even numbers from a list of numbers"""
    even_numbers=[]
    for number in numbers:
        if number%2==0:
              even_numbers.append(number)
              
    return [x for x in even_numbers]