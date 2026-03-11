# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 21:38:18 2025

@author: Surface
"""

def multiply_numbers(*numbers):
    """This functions gives products of all given numbers"""
    product=1
    for n in numbers:
        product*=n
    return product
print(multiply_numbers(1,2)) # 2
print(multiply_numbers(2,3,6,4,1)) # 144
print(multiply_numbers(21,31,2,0)) # 0

def students_info(name,l_name,**information):
    """This function gives details about students"""
    information['name']=name
    information['last name']=l_name
    return information
student1=students_info('akbar','rahmonov',b_year=2008)
student2=students_info('husan','kamolov',b_year=2007,b_place='kokand',
                       subject='algebra')
print(student1)
print(student2)
        

