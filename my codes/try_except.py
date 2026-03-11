# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 09:47:34 2025

@author: Surface
"""

#age = input('Enter your age:')
#try:
#   age=int(age)
#   byear=2025-age    
#except ValueError:
#    print('Enter integer:')
#else:
#    print(byear)
     
sonlar=[12,23,65.8,34,97.3,73,]
for x in sonlar:
      if isinstance(x,float):
          print('This is a float number')
      else:
          print(int(x))
          
guests=['abdulloh','akbar','olim','shohrux','hasan','husan']

try:
    print(guests[4])
except:
    print(f'This list has only {len(guests)} ')
  
    
student2={'name':'akbar','lastname':'hasanov','major':'math'}
student3={'name':'olim','lastname':'salimov','major':'AI'}

import json

with open('student2.json','w') as f:
    json.dump(student2,f)
with open('student3.json','w') as f:
    json.dump(student3,f)
students=['student1.json','student2.json','student3.json','student4.json','student5.json'] 
for filename in students:
    try:
        with open(filename) as f:
            student = json.load(f)
    except:
        print(f'This {filename} is not available')
    else:
        print(f'{student['name']} {student['lastname']}')
        
with open('names.json','w') as f:
    json.dump(student2['name'],f)
    json.dump(student3['name'],f)

    
            

    