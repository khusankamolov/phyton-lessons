# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 10:28:12 2025

@author: Surface
"""

class User:
    """This class gives details about the user"""
    def __init__(self,name,l_name,b_year,b_place,email):
        self.name=name.title()
        self.lastname=l_name.title()
        self.birthyear=b_year
        self.birthplace=b_place.title()
        self.email=email
    def get_info(self):
       return (f"User is {self.name} {self.lastname} who was born in {self.birthplace}"
       f" in {self.birthyear}, and email: {self.email}.")
    def get_age(self,year):
        return year-self.birthyear
    def get_lastname(self):
        pass
    def get_b_place(self):
        return self.birthplace
user1=User('Husan','Kamolov',2008,'Kokand','husankamolov27@gmail.com')
user2=User('akbar','husanov',2002,'toshkent','akhusan23@gmail.com')
user3=User('abdulloh','javlonov',2005,'samarqand','abdullohjv2@gmail.com')
print(user1.get_info())
print(user2.get_info())
print(user3.get_info())

class Select_Student:
    """This class gives name of students who get high scores"""
    def __init__(self,name,lastname,gradelevel,exam,score):
        self.name=name.title()
        self.l_name=lastname.title()
        self.g_level=gradelevel
        self.exam=exam.upper()
        self.score=score
    def select(self):
        if self.exam == 'SAT':
            if self.score>=1400 and self.score<=1600 :
                return (f"{self.name} {self.l_name} passed the exam"
                      f" in {self.g_level} grade level with {self.score} in SAT.")
            elif self.score<1400:
                return (f"{self.name} {self.l_name} did not pass the exam"
                      f" in {self.g_level} grade level with {self.score} in SAT.")
            else: 
                return "It is impossible to get higher than 1600 in SAT."
            
        elif self.exam == 'IELTS':
            if self.score>=7 and self.score<=9:
                return (f"{self.name} {self.l_name} passed the exam"
                      f" in {self.g_level} grade level with {self.score} in IELTS.")
            elif self.score<7:
                return (f"{self.name} {self.l_name} did not pass the exam"
                      f" in {self.g_level} grade level with {self.score} in IELTS.")
            else:
                return "It is impossible to get higher than 9 in IELTS."
           
        else:
            return f"We don't require {self.exam} test!"
student1=Select_Student("Alijon",'Gafurov',11,'sat',1600)
student2=Select_Student("jonatan",'uik',9,'ielts',8.5)
print(student1.select())
print(student2.select())
       
        
            
