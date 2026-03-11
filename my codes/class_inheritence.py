# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 11:00:56 2025

@author: Surface
"""

class User:
    """This class gives details about the user"""
    num_users=0
    def __init__(self,name,l_name,b_year,b_country,email):
        self.name=name.title()
        self.lastname=l_name.title()
        self.birthyear=b_year
        self.birthcountry=b_country.title()
        self.__email=email
        User.num_users+=1
        
    @classmethod
    def get_num_users(cls):
        return cls.num_users
    def get_info(self):
       return (f"{self.name} {self.lastname} was born in {self.birthcountry}"
       f" in {self.birthyear}, and email: {self.email}.")
    def get_age(self,year):
        return year-self.birthyear
    def get_lastname(self):
        pass
    def get_b_place(self):
        return self.birthcountry
    def get_email(self):
        return self.__email


class Student(User):
    """This class saves deatils about the student"""
    __num_students=0
    def __init__(self, name, l_name, b_year, b_country, email,idnumber):
        super().__init__( name, l_name, b_year, b_country, email)
        self.idnumber=idnumber
        self.bosqich = 1
        self.lessons = []
        Student.__num_students+=1
        
    @classmethod
    def get_num_students(cls):
        return cls.__num_students
    def get_info(self):
           return (f"{self.name} {self.lastname} was born in {self.birthcountry}"
           f" in {self.birthyear}, and email: {self.email} . Id Number: {self.idnumber}")
        
    def set_bosqich(self,bosqich):
        self.bosqich=bosqich
        
    def get_bosqich(self):
        return self.bosqich
    
    def write_courses(self,x):
       for subject in x.__dict__.values():
           self.lessons.append(subject)
       
    def get_lessons(self):
        return self.lessons
    
    def remove_subject(self,subject):
        if subject in self.lessons:
            self.lessons.remove(subject)
        else:
            return "You don't have this subject in your course schedule!"
class Fan:
    """This class gives the list of lessons"""
    def __init__(self,math,english,chemistry,history,informatics):
        self.math=math
        self.chemistry=chemistry
        self.english = english
        self.history=history
        self.informatics=informatics
    

#student1=Student('husan','kamolov',2008,'uzbekistan','husan.2@gmail.com','FI929320192')  
#student2=Student('hasan','kamolov',2006,'germany','hasan.2@gmail.com','FI928620192')   
 
#student_subjects=Fan('advanced math','IELTS','chemistry','national history','computer science')

class Professor(User):
    """This class covers details about the professor"""
    def __init__(self,name,l_name,b_year,b_country,email,job,major):
        super().__init__( name, l_name, b_year, b_country, email)
        self.job=job
        self.major=major
        self.__work_years=0
    def add_work_years(self,year):
        if year>=0:
           self.__work_years+=year
        else:
            print("You can't decrease work years!")
    def get_work_years(self):
        return self.__work_years
            
    def get_major(self):
        return self.major
    
   
    def get_info(self):
        info= f"{self.name} {self.lastname} is from {self.birthcountry}. Degree- PHD in {self.major}, "
        info+=f"{self.work_years} year work experience with being {self.job}."
        return info
#professor1=Professor('Anvar','nazrullayev',2000,'america','anvar3@gmail.com','teacher','AI')    


class Worker(User):
      """This class has details about the worker"""
      def __init__(self,name,l_name,b_year,b_country,email,work_hours,workplace,salary):
          super().__init__(name,l_name,b_year,b_country,email)
          self.__work_hours=work_hours
          self.workplace=workplace
          self.salary=salary
          self.work_years=0
      def get_info(self):
          info = f"{self.name} {self.lastname} is from {self.birthcountry},"
          info+= f" email: {self.email}. Daily work hours - {self.work_hours}, Salary - {self.salary}$,"
          info+= f" Work years - {self.work_years} and workplace is {self.workplace}. "
          return info
      def get_work_hours(self):
          return self.__work_hours
      def get_workplace(self):
          return self.workplace
      def get_salary(self):
          return self.salary
      def get_work_years(self):
          return self.work_years
      def set_work_years(self,year):
          self.work_years=year
    
          
          
class Workplace:
    """This class gives location of a workplace"""
    def __init__(self,country,region,city,street):
        self.country=country.title()
        self.region=region.title()
        self.city=city.title()
        self.street=street.title()
    def get_workplace(self):
        return f"in {self.street} in {self.city} in {self.region},{self.country}"
        
workplace1=Workplace('uzbekistan','fergana','kokand','sharqobod')
worker_office=workplace1.get_workplace()
#worker1=Worker('abdulloh','kamolov',2005,'australia','abdulloh25@gmail.com',7,worker_office,12000)

class Customer(User):
    """This class cover all details about the customer"""
    def __init__(self, name, l_name, b_year, b_country, email,expenses,satisfy_level,gender):
        super().__init__(name, l_name, b_year, b_country, email)
        self.expenses=expenses
        self.s_level=satisfy_level
        self.gender=gender
        self.products=[]
    def get_info(self):
        info= f"{self.name} {self.lastname}  is {self.gender} and from {self.birthcountry}."
        info+=f"Satisfying degree - {self.s_level}, Expenses - {self.expenses}$,"
        info+="Products: "
        for x in self.products: info+=f"{x}, "
        return info
    def add_product(self,product):
        self.products.append(product)
    def get_products(self):
        return self.products
    def get_gender(self):
        return self.gender
    def get_expenses(self):
        return self.expenses
    def get_slevel(self):
        return self.s_level
#customer1=Customer('davron','turdiyev',1998,'uzbekistan','davron2@gmail.com',60,'good','male')
    
class Winner(Customer):
    """This class gives details about winner from customers"""
    def __init__(self, name, l_name, b_year, b_country, email,expenses,satisfy_level,gender,award_money,day,month):
        super().__init__(name, l_name, b_year, b_country, email,expenses,satisfy_level,gender)
        self.award=award_money
        self.day=day
        self.month = month
    def get_info(self):
        info= f"{self.name} {self.lastname}  is {self.gender} and from {self.birthcountry}."
        info+=f"Award money - {self.award}$, Date - {self.day} {self.month.title()}."
        return info
    def get_profit(self):
        return self.award-self.expenses
    def get_award(self):
        return self.award
    
#winner1=Winner('lola','malikova',2002,'uzbekistan','lola32@gmail.com',200,'good','female',20000,19,'november')
        