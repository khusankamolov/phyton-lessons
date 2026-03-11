# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 12:16:31 2025

@author: Surface
"""

class Car():
    """This class cover all details about the car"""
    def __init__(self,model,color,transmission,cost,produced_year):
        """The properties of the car"""
        self.model=model
        self.color=color
        self.transmission=transmission
        self.cost=cost
        self.p_year=produced_year
        self.km=0
    def get_info(self):
        """This function gives full information of the car"""
        if self.model.lower()=='bmw':
           self.model=self.model.upper()
        else:
           self.model= self.model.title()
        return (f"{self.model} is produced in {self.p_year},"
               f" and its color: {self.color}; its transmission: {self.transmission};"
               f" its cost and kilometr are {self.cost}$ and {self.km} km,respectively.")
        
    def update_km(self):
       self.km+=1
    def set_km(self,kilometr):
        self.km=kilometr
       
    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def get_transmission(self):
        return self.transmission
    def get_cost(self):
        return self.cost
    def get_p_year(self):
        return self.p_year
    def get_km(self):
        return self.km
    
       

car1=Car('hyundai','red','automatic',12000,2006)
car2=Car('BMW','silver','automatic',230000,2025)
car3=Car('bugatti','orange','mechanic',13000,1998)
#print(car1.get_info())
#print(car2.get_info())


class Car_Dealership():
    """This class gies information about cars in the car dealership"""
    def __init__(self,name,address,founded_year,country):
        """This function gives several deatails about the car dealership"""
        self.name=name.title()
        self.address=address.title()
        self.f_year= founded_year 
        self.country=country.title()
        self.cars=[]
        self.cars_number=0
    def get_info(self):
        """This function shows every details about the car salon"""
        return (f"{self.name} is a car dealership which was founded in"
                f" {self.founded_year} and is located in {self.address}"
                f" in {self.country}")
    def add_car(self,car):
        self.cars.append(car)
        self.cars_number +=1
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_fyear(self):
        return self.f_year
    def get_country(self):
        return self.country
    
    def get_cars(self):
        return [car.get_info() for car in self.cars]
    def get_cars_num(self):
        return self.cars_number
    
carpark=Car_Dealership('chevrolet','andijan',1995,'uzbekistan')

carpark.add_car(car1)
carpark.add_car(car2)
carpark.add_car(car3)
print(carpark.get_cars())

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]