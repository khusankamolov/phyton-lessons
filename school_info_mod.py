# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 19:01:56 2025

@author: Surface
"""

def school_info(name,f_year,n_students,major,n_teachers=None):
    """This function gives details of a school as dictionaries"""
    school={'name':name,
            'f_year':f_year,
            'n_students':n_students,
            'major':major,
            'n_teachers':n_teachers}
    return school

def school_enter():
    """This function asks user details of the school and adds them in a dictionary"""
    schools=[]
    while True:
        print('\nEnter these details')
        name=input('Enter name of the school: ')
        f_year=int(input('Enter the foundation year of the school: '))
        n_students=int(input('Enter the number of students at the school: '))
        major=input('Enter teh major subject of the school: ')
        n_teachers=int(input('Enter the number of teachers:  '))
        schools.append(school_info(name,f_year,n_students,major,n_teachers))
        answer=input('Do you want to add another school?: (yes/no)')
        if answer=='no':
            break

def school_print(school_info):
    """This function shows all details of a school which are given by the user"""
    print(f"{school_info['name'].title()} is founded in {school_info['f_year']} "
          f"and its major subject is {school_info['major']}. "
          f"It has {school_info['n_students']} students and the number of its "
          f"teachers is {school_info['n_teachers']}.")
    