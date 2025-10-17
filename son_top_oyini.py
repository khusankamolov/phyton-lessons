# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 19:26:04 2025

@author: Surface
"""


print("\nKeling o'ylagan sonni topish o'yinini o'ynaymiz!!!")
import random as r
def son_top(x=10):
    tahminlar=0
    son=r.randint(1,x)
    savol=int(input(f"1 dan {x} gacha son o'yladim. Topa olasizmi?\n>>>"))
    while True:
        tahminlar+=1
        if son<savol:
          savol=int(input("Xato,men o'ylagan son bundan kichikroq."
                        "Yana harakat qiling:\n>>>"))
        elif son>savol:
          savol=int(input("Xato,men o'ylagan son bundan kattaroq."
                        "Yana harakat qiling:\n>>>"))
        else: 
            print(f"TOPDINGIZ! {son} sonini oylagan edim. {tahminlar} ta tahmin bilan"
                 f" topdingiz. Tabriklayman!")  
            break
    return tahminlar





def son_top_pc(x=10):
    tahminlar2=0
    input(f"\n1 dan {x} gacha son o'ylang. Men topishga harakat qilaman.Agar son o'ylagan"
          " bo'lsangiz,istalgan tugmani bosing.")
    quyi=1
    yuqori=x
    while True:
        tahminlar2+=1
        if quyi!=yuqori:
            tahmin=r.randint(quyi,yuqori)
        else:
            tahmin=quyi
        javob=input(f"Siz {tahmin} sonini o'yladingiz: to'g'ri(T),"
                "men o'ylagan son bundan kattaroq(+),yoki kichikroq(-)".upperT())
        if javob=='-':
           yuqori=tahmin-1
        elif javob=="+":
           quyi=tahmin+1
        elif javob=='T':
           break
    
    print(f"Soningizni {tahminlar2} ta tahmin bilan topdim!")
    return tahminlar2



def play(x=10):
    yana=True
    while yana:
      tahminlar_user=son_top()
      tahminlar_pc=son_top_pc()
      if tahminlar_user>tahminlar_pc:
            print("Siz yutqazdingiz,men yutdim.")
      elif tahminlar_user<tahminlar_pc:
            print("Siz yutdingiz!Men yutqazdim.")
      else:
            print(f"Durrang.Ikkimiz ham {tahminlar_user} ta tahmin qildik.")
      yana=int(input("Yana o'ynashni xohlaysizmi? (ha(1)/yo'q(0)):"))
      
play()
    
    
    

    