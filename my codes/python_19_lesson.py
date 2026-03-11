# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 15:54:10 2025

@author: Surface
"""

def ism_yosh(ism,yosh):
    """Foydalanuvchining ism va yoshini sorash orqali tug'ilgan yilni hisoblash
    formulasi"""
    print(f"Salom, {ism.title()}.Siz {2025-yosh}yilda tug'ilgansiz.")
#ism_yosh('husan',25)
#ism_yosh('anvar',12)
def kvad_kub(son):
    """Foydalanuvchidan son olib uni kvadrati kubini hisoblovchi funksiya"""
    print(f"{son}ning kvadrati {son**2}ga teng va "
          f"uning kubi {son**3}ga teng")
#kvad_kub(2)
#kvad_kub(54)
#kvad_kub(235)
def even_odd(number):
    """This function finds a number as even or odd by accepting it from user"""
    if number%2==0:
        print(f"{number} is even.")
    else:
        print(f'{number} is odd.')
#even_odd(8)
#even_odd(5) 
#even_odd(78)
def big_small(x,y):
    """This function compares two numbers given by the user and finds 
    which of them is bigger or smaller"""
    if x>y:
        print(f"{x} is bigger than {y}.")
    elif x<y:
        print(f"{x} is smaller than {y}.")
    else:
        print("Both of them are equal.")
#big_small(76,93)
#big_small(44,44)
#big_small(-45,-32)
#big_small(54**2,453*5)
def exponent(x,y): # 'exponent' bu 'daraja' dean manoni bildiradi
    """This function calculates (x**y) by getting their values from the user"""
    print(f"{x} to the exponent of {y} is equal to {x**y}.")
#exponent(3,4)
#exponent(-5,2)
#exponent(2*3,3)
def power(x,y=2): # 'power'  tarjimasi 'daraja' degani
    """This function calculates x squared 
    by getting a value of x from the user"""
    print(f"{x} squared is equal to {x**2}.")
#power(2,2)
#power(23)
#power(-5)
def bolinish_alomatlari(son):
    """This function checks which numbers from 2 to 10 divide a given number 
    without remainder"""
    for z in range(2,11):
        if son%z==0:
            print(f"{son} is divided by {z} without remainder. ")
bolinish_alomatlari(12)
bolinish_alomatlari(35)
bolinish_alomatlari(79)

    
    

