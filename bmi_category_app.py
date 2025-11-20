# -*- coding: utf-8 -*-
"""
App name:
    BMI calculation and classification
"""

def calculate_bmi(weight,height):
    """This function calculate BMI by using given height(sm) and weight(kg)"""
    height_m=height/100  #change height from sm to metr
    
    bmi=weight/(height_m**2)
    return bmi

def bmi_category(bmi):
    """This function identifies a situation with the measure of BMI"""
    if bmi<18.5:
        return "Low weight"
    elif 18.5<=bmi<25:
        return "Healthy weight"
    elif 25<=bmi<30:
        return 'Overweight'
    else:
        return 'Obesity'


weight=float(input("Enter your weight (kg): "))
height=float(input('enter your height (sm): '))

bmi=calculate_bmi(weight, height)
category=bmi_category(bmi)

print(f"Your BMI: {bmi}")
print(f"Your BMI category: {category}")