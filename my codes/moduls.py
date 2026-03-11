# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 21:16:44 2025

@author: Surface
"""

#import math
#x=256
#print(math.sqrt(x))
#print(math.pow(4,3))
#print(math.pi)
#print(math.log2(16))
#print(math.log(9,3))

import random as r

 #randint()
number=r.randint(0,90)
print(number)

 #choice()
numbers=list(range(20,100,4))
print(r.choice(numbers))

names=['ali','jon','alisa','kamol','johongir']
print(r.choice(names))

 #shuffle()
numbers1=list(range(20))
print(numbers1)
r.shuffle(numbers1)
print(numbers1)