# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 10:43:06 2025

@author: Surface
"""

p_i_lugat={}
p_i_lugat['if']='agar'
p_i_lugat['else']='aks holda'
p_i_lugat['string']='matn'
p_i_lugat['integer']='butun son'
p_i_lugat['float']="o'nlik son"
p_i_lugat['variable']="o'zgaruvchi"
p_i_lugat['length']='uzunlik'
p_i_lugat['append']="qo'shmoq"
p_i_lugat['remove']="o'chirmoq"
p_i_lugat['input']='kiritmoq'

#for key,value in sorted(p_i_lugat.items()):
  #  print(f'{key.title()} - {value.lower()}')
davlat_poytaxt={'o\'zbekistan':'toshkent','rossiya':'moskva','xitoy':'pekin',\
'fransiya':'paris','amerika':'washington','tojikiston':'dushanbe',\
'britanya':'london'}
#print('Dunyo davlatlari:')
#for k in sorted(davlat_poytaxt):
#    print(f'{k.upper()}')
#print('\nDavlatlar poytaxtlari:')
#for q in sorted(davlat_poytaxt.values()):
#    print(f'{q.title()}')
#for davlat,poytaxt in davlat_poytaxt.items():
  #  print('Bizda bunday malumot yo\'q')
#else:
#    print(f'{davlat.title()}ning poytaxti {davlat_poytaxt[davlat].title()}')
#davlat=input('Qaysi davlat poytaxtini bilishni xohlaysiz?:').lower()
#poytaxt=davlat_poytaxt.get(davlat)
#if poytaxt==None:
#    print('Bizda bunday malumot yo\'q')
#else:
#   print(f'{davlat.title()}ning poytaxti {poytaxt.title()}')
menu={'shorva':10000,'mastava':27000,'kabob':13000,'osh':15000,\
      'tovuq':30000,'salat':20000,"perashki":3000,'hot-dog':10000,'choy':5000,\
      'baliq':40000}
buyurtmalar=[]
print('Uchta taom buyurtma bering:')
for n in range(3):
    buyurtmalar.append(input(f'{n+1}-taom:').lower())
for buyurtma in buyurtmalar:
  if buyurtma in menu:
    print(f'{buyurtma.title()} {menu[buyurtma]}so\'m')
  else:
    print('Kechirasiz bizda bunday taom yo\'q')