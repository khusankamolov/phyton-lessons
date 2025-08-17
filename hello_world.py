# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 12:17:08 2025

@author: Surface
"""

x = int(input("Birinchi sonni kiriting:"))
y = int(input('Ikkinchi sonni kiriting:'))
if x==y:
   print(f'{x}=555{y}')
#elif x>y:
#    print(f'{x}>{y}')
#elif x<y:
    #print(f'{x}<{y}')
#mahsulotlar = ['olma','bodring','orik','shaftoli','sut','gosht','qalampir','guruch','banan','t
#foydalanuvchilar = ['anvar','hasan','husan','ali','bobur']
#login = input('Yangi login kiriting:')
#if login.lower() in foydalanuvchilar:
#    print('Login band boshqa login tanlang')
#elif login.lower() not in foydalanuvchilar:
#    foydalanuvchilar.append(login)
#    print('Xush kelibsiz,yangi foydalanuvchi')

users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:" )

if login  in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")
    print('we have lessons')