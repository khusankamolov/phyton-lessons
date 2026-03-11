# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 09:35:46 2025

@author: Surface
"""

#from math import sqrt as s
#ildiz=lambda x: s(x)
#numbers=list(range(20))
#ildizlar=(list(map(ildiz,numbers)))
#print(ildizlar)

#import math 
#=[3,4,5]
#b=[6,2,8]
##a_plus_b=list(map(lambda x,y:(x+y)**2,a,b))
#print((a_plus_b))

cars=['bugatti','lambarghini','honda','mustang','matiz','kobalt']

car_m=list(filter(lambda car:car.startswith('m'),cars))
print(car_m)
car_5=list(filter(lambda car: len(car)>=6 and car.endswith('i'),cars))
print(car_5)

import random as r
sonlar=list(r.sample(range(50),10))
#odd=list(filter(lambda x:x%2!=0,sonlar))
#print(sonlar)
#print(odd)

def karrali3(x):
    """This function numbers which is divided by 3"""
    return x%3==0
divide3=list(filter(karrali3,sonlar))
print(sonlar)
print(divide3)

def summa(k):
    return lambda x: x+k
yigindi2=summa(2)
addition=list(map(yigindi2,sonlar))
print(addition)

def tubmi(x):
    if x%2==0 or x<2:
        return False
    if x==2 or x==3:
        return True
    for i in range(3,x,2):
        if x%i==0:
            return False
    return True
tub_sonlar=list(filter(tubmi,range(100)))
print(tub_sonlar)
    
def fiboninchi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
fiboninchi_sonlar=fiboninchi(10)
print(fiboninchi_sonlar)