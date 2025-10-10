# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 19:29:21 2025

@author: Surface
"""
#son=0
#while son<10:
#    son+=1
#    if son%2!=0:
#        print(son)
buyurtmalar=[]
savol="Nima buyurtma berasiz?:"
#while True:
#    buyurtma=input(savol)
#    buyurtmalar.append(buyurtma)
#    takrorlash=input('Yana buyurtma berasizmi? (ha/yo\'q):')
#    if takrorlash =="yo'q":
#        break
#for buyurtma in buyurtmalar:
#    print(buyurtma)

e_bozor_mahsulotlar={}
#savol='\nMahsulotning nomini kiriting:'
#ishora=True
#while ishora:
#    mahsulot=input(savol)
#    narh=input(f'{mahsulot.title()}ning narhi qancha?:')
#    e_bozor_mahsulotlar[mahsulot]=int(narh)
#    javob=input("Yana mahsulot qo'shasizmi?: (ha/yo'q)")
#    if javob!='ha':
#        ishora=False
#for mahsulot,narh in e_bozor_mahsulotlar.items():
#    print(f"{mahsulot.capitalize()}ning narhi {narh} so'm \n")

#if buyurtmalar:
#    for buyurtma in buyurtmalar:
#        if buyurtma in e_bozor_mahsulotlar.keys():
#           print(f"{buyurtma.capitalize()} {e_bozor_mahsulotlar[buyurtma]} so'm")
#        else:
#           print(f"Kechirasiz bizda {e_bozor_mahsulotlar[buyurtma]} yo'q")
           
#while buyurtmalar:
#    buyurtma = buyurtmalar.pop()
#    if buyurtma in e_bozor_mahsulotlar.keys():
#        narh=e_bozor_mahsulotlar[buyurtma]
#        print(f"{buyurtma.capitalize()} - {narh} so'm")
#    else:  print(f"Bizda {buyurtma} yo'q")

mehmonlar={'abdulloh','akbarshoh','nigoraxon ustoz','nigina','alijon',
           'olimxon'}
#while mehmonlar:
#    mehmon=mehmonlar.pop()
#    print(f"Salom {mehmon.capitalize()}, bugun bayramga keling.")

b_taomlar=[] 
menu={'osh':15000,"sho'rva":20000,'kabob':13000,'mastava':24000,"lag'mon":8000}
savol="Nima taom buyurtma berasiz?"
while True:
    taom=input(savol)
    b_taomlar.append(taom)
    takrorlash=input("Yana ovqat buyurasizmi? (ha/yo'q):")
    if takrorlash != 'ha':
        break
for taom in b_taomlar:
    print(f"{taom} \n")

while b_taomlar:
    taom=b_taomlar.pop()
    if taom in menu:
        narh=menu[taom]
        print(f"{taom.capitalize()} - {narh} so'm")
    else:
        print(f"Kechirasiz, bizda {taom} yo'q.")
        
        

      

    