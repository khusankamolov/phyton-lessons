# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 11:30:22 2025

@author: Surface
"""

from transliterate import to_cyrillic,to_latin
matn=input("Enter a text:")
if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))