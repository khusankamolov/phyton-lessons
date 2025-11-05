# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 14:36:17 2025

@author: Surface
"""

def selectbig(x,y,z):
    """This function select biggest one among three numbers"""
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z
    
    
    