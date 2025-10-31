# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 10:08:15 2025

@author: Surface
"""

from people import User, Student, Professor

student=Student('akbar','Boburov',1998,'spain','akbar24@gmail.com','FI12345677')
user=User('olim','hakimov',2015,'uzbekistan','olim@gmail.com')
professor=Professor('sobir','jabborov',2000,'tajikistan',"sobir34@gmail.com",'economist','ecology')
print(student.get_age(2025))
print(user.get_email())
print(user.get_num_users())
print(student.get_num_students())
professor.add_work_years(23)
print(professor.get_work_years())
print(professor.get_info())