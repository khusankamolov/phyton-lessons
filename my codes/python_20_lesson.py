# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 14:37:10 2025

@author: Surface
"""

#def customer_info(name,l_name,b_year,b_city,e_address='',p_number=None):
#    """This function gives details about customer"""
#    customer= {'name':name,
#           'l_name':l_name,
#           'age':2025-b_year,
#           'b_city':b_city,
#           'email':e_address,
#           'p_number':p_number}
#    return customer

#print('Enter details about the customer:')
#customers=[]
#while True:
#    name=input('His/her name:')
#    l_name=input("His/her last name:")
#    b_year=int(input('His/her birth year:'))
#    b_city=input('His/her birth place:')
#    email=input('His/her email:')
#    p_number=input('His/her phone number:')
#    customers.append(customer_info(name,l_name,b_year,b_city,email,p_number))
#    answer=input('Do you want to add another customer? (yes/no)')
#    if answer=='no':
#        break
#print("Customers' details")   
#for customer in customers:
#    gender=input('Customer is male or female:')
#    if gender=='male':
#       print(f"{name.title()} {l_name.title()} was born in {b_city.title()}, and "
#             f"his phone number and email are {p_number} and {email},respectively. ")
#    else:
#        print(f"{name.title()} {l_name.title()} was born in {b_city.title()}, and "
#              f"her phone number and email are {p_number} and {email},respectively. ")

#def comparing_number(number1,number2,number3):
#   """This function show the biggest number among 3 numbers"""
#    if number1>=number2 and number1>=number3:
#       print(number1)
#    elif number2>=number1 and number2>=number3:
#        print(number2)
#    else:
#        print(number3)
#number1=input('write 1-number:')
#number2=input('write 2-number:')
#number3=input('write 3-number:')
#comparing_number(number1,number2,number3)

#details_of_circle={}
#radius=float(input('Enter radius of the circle:'))
#pi=3.14
#diametr=radius*2
#perimetr= 2*pi*radius
#area=pi*(radius**2)
#def circle_info(radius):
#    """This function gives radius,diametr,perimetr and area of a circle by accepting 
#     its radius from a user"""
#    circle={'radius':radius,
#     'diametr':diametr,
#     'perimetr':perimetr,
#     'area':area}
#    return circle
#for detail,answer in circle_info(radius).items():
#    print(f'{detail.title()} - {answer}')


#def find_prime_numbers(min, max):
#    prime_numbers = []
#   for n in range(min, max + 1):
#        prime = True
#        if n == 1:
#            prime = False
#        elif n == 2:
#            prime = True
#        else:
#            for x in range(2, n):
#                if n % x == 0:
#                    prime = False
#        if prime:
#            prime_numbers.append(n)
#    return prime_numbers
#prime_numbers=find_prime_numbers(2,43)
#print(prime_numbers)
def fiboninchi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
print(fiboninchi(10))
        

     
     

           
    