# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 10:49:16 2025

@author: Surface
"""

import datetime as dt
today=dt.datetime.now()
#print(today)
day1=dt.datetime(2025,11,22)
day2=dt.datetime(2025,12,6)
day3=dt.datetime(2025,12,20)
day4=dt.datetime(2025,1,3)
day5=dt.datetime(2025,1,17)
day6=dt.datetime(2025,2,1)
day7=dt.datetime(2025,2,15)
day8=dt.datetime(2025,3,1)
day9=dt.datetime(2025,3,15)
day10=dt.datetime(2025,3,29)


ramazon=dt.datetime(2026,2,18)
farq1=ramazon-today
seconds1=farq1.seconds
minutes1=int(seconds1/60)
hours1=int(minutes1/60)
#print(f"There are {farq1.days} days and {hours1} hours until Ramadhan. ")

qurbonhayit=dt.datetime(2026,5,27)
farq2=qurbonhayit-today
seconds2=farq2.seconds
minutes2=int(seconds2/60)
hours2=int(minutes2/60)
days2=farq2.days
#print(f"There are {days2} days, {hours2} hours, and {minutes2} minutes until Kurban Hayid. ")

def mybirthday(year,month,day,hour,minute):
   mybirthday=dt.datetime(year,month,day,hour,minute)
   difference=today-mybirthday
   print(difference)
   days=difference.days
   years=float(days/365)
   months=float(years*12)
   daysleft=int((months-int(months))*30)
   print(f"There have been {int(years)} years, {int(months)} months, and {daysleft} days since my birthday. ")
#mybirthday(2008,11,19,11,30)

import re
#phone_num=input('Please, enter your phone number:')
#andoza='^\+998\d{9}$'
#if re.match(andoza,phone_num):
#    print("Your phone number is accepted")
#else:
#    print("You don't enter a proper phone number")
    
text=""""Our systems have detected unusual traffic from your computer network. This page checks to see if it's really you sending the requests, and not a robot. Why did this happen?
IP address: 151.115.98.4
Time: 2025-11-09T05:12:00Z
URL: https://www.youtube.com/watch?v=vsxJPRLXpgI&feature=youtu.be"""
pattern = r'https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*'
url=re.findall(pattern,text)
print(url)
   
from pprint import pprint
import json 
with open('student2.json','r') as f:
    student=json.load(f)
pprint(student)
with open('api-result.json') as f:
   result=json.load(f) 
pprint(result)
    
    
    
    