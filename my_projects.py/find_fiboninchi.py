# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 15:41:08 2025

@author: Surface
"""

def fiboninchi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
numbers=fiboninchi(1000)
def find_fibonin(x):
    if x in numbers:
        return True
    else:
        return False
    
        