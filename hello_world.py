# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 12:17:08 2025

@author: Surface
"""
onam = {'ism':'feruzaxon','yosh':'52','t_joy':"farg'ona"}
#print(f"Mening onam {onam['ism'].title()} \
#{onam['yosh']}yoshdalar va {onam['t_joy'].title()}da tug'ilganlar.")
oila_taom = {'onam':'mastava','dadam':'sho\'rva','hasan':'kabab','abubakr':'kchiri',
             'sharifaxon':'osh'}
#print(f"Onamning sevimli ovqatlari {oila_taom['onam']}")
#print(f"Dadamning sevimli ovqatlari {oila_taom['dadam']}")
#print(f"Akamning sevimli taomi {oila_taom['abubakr']}")
#print(f"Hasanning sevimli taomi {oila_taom['hasan']}")
#print(f"Opamning sevimli taomi {oila_taom['sharifaxon']}")
i_lugat = {'integer':'butun son','float':"o'nlik son",'list':'sansh uchun',
           'if':'agar','string':'matn','get':'olmoq',
           'input':'konsolga chiqarish uchun','elif':"if ga qo'shimcha",
           'else':'bunday bolmasa','append':"qo'shmoq"}
soz = input("Kalit so'z kiriting:").lower()
#if soz.lower() in i_lugat:
    #print(f"Ushbu kalit so'z {soz.lower()} {i_lugat[soz.lower()].lower()} deb tarjima qilinadi")
#else:
  #   print("Bunday so'z mavjud emas")
tarjima = i_lugat.get(soz)
if tarjima == None:
    print('Bunday so\'z mavjud emas')
else:
    print(f"{soz.title()} sozi {tarjima.lower()} deb tarjima qilinadi.")