# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 11:27:43 2025

@author: Surface
"""

onam = {'ism':'feruzaxon','yosh':53,'t_yil':1974,'viloyat':'fargona'}
#print(f"Mening onam {onam['ism'].title()} {onam['t_yil']} yilda \
#{onam['viloyat'].title()}da tug\'ilgan va uning yoshi {onam['yosh']}da.")
s_taomlar={'otam':'mastava','onam':'osh','akam':'kchiri','apam':'shorva',\
           "opoqim":'lagmon'}
#print(f"Otamning sevimli taomi {s_taomlar['otam']}.\
#Akamning sevimli taomi {s_taomlar['akam']}.\
#Opoqimning sevimli taomi {s_taomlar['opoqim']}.")
#for key in s_taomlar:
#   print(f"{key.title()}ning sevimli taomi {s_taomlar[key]}.")
lugatlar={'integer':'butun son','float':'onlik son','if':'agar',\
          'else':'aks holda','string':'matn','variable':'ozgaruvchi',\
        'length':'uzunlik','append':'qoshmoq','remove':'ochirmoq','type':'tur'}
key=input("Kalit so'zni kiriting:").lower()
#if key.lower() in lugatlar:
 #       print(f"Bu kalit so'zning tarjimasi {lugatlar[key.lower()]})
#else:
 #      print("Bunday kalit so'z mavjud emas")      
#value=lugatlar.get(key,"Bunday kalit so'z mavjud emas" )
#print(value)
tarjima=lugatlar.get(key)
if tarjima==None:
    print("Bizda bunday kalit so'z mavjud emas.")
else:
    print(f"'{key.title()}' kalit so'zning \
tarjimasi {tarjima}.")
