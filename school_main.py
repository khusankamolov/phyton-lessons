# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 21:31:04 2025

@author: Surface
"""

import school_info_mod
school1 = school_info_mod.school_info('cambridge',1997,13000,'math',1200)
school_info_mod.school_print(school1)

import school_info_mod as sim
school2=sim.school_info('1-specialized school',2022,200,'algebra',46)
sim.school_print(school2)

from school_info_mod import school_info,school_print
school3=school_info('al_xorazmiy',1778,9800,'math')
school_print(school3)

from school_info_mod import school_info as si, school_print as sp
school4=si('beruniy',2000,1280,'chemistry',270)
sp(school4)

#from school_info_mod import *
#school5 =school_info('harvard',1912,14000,'business',2000)
#school_print(school5)
from find_word_games import play
play()