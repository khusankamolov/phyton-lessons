# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 21:09:45 2025

@author: Surface
"""

def big_letter(names):
    """This function changes first letter of names to a big letter"""
    for n in range(len(names)):
        names[n]=names[n].capitalize()
    return names
names=['ali','vali','jonny','alisa','jennifer']
title_names=big_letter(names[:])
print(names)
print(title_names)

def grade(names):
    """This function gives a student's name with his grade as a dictionary"""
    grades={}
    for name in names:
        grade=input(f"Enter {name.title()}'s grade:")
        grades[name]=grade     
    return grades
students=['akbar','rustam','dilshod','farhod','hojakbar']
grades=grade(students)
print(grades)
        