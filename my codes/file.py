# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 11:30:15 2025

@author: Surface
"""

with open('pi_million_digits.txt') as file:
    pi=file.read()
    
pi=pi.rstrip()
pi=pi.replace('\n','')
pi=pi.replace(' ','')
bdate='19112008'
#print(bdate in pi)
#pi=float(pi)

import pickle
with open('new_file.dat','wb') as file:
    pickle.dump(pi,file)

#while True: 
#     car=input('What is your favourite car?')
#     with open('data.txt','a') as file:
#            file.write(car+'\n')
#     repeat = input('Do you want add another car? (yes/no):')
#     if repeat=='no':
#         break
avto1={'model':'hyundai','color':'red','transmission':'automatic','year':2005}
avto2={'model':'chevrolet','color':'black','transmission':'automatic','year':2025}

with open('info.txt','wb') as file:
    pickle.dump(avto1,file)
    pickle.dump(avto2,file)
with open('info.txt','rb') as file:
    avto1=pickle.load(file)
    avto2=pickle.load(file)
#with open('info.txt','a+') as file:
#    file.write('damas'+'\n')
#    file.write('mustang'+'\n')
    
    
