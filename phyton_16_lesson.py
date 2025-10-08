# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 10:11:54 2025

@author: Surface
"""
alloma0={'ism':'alisher','familiya':'navoiy','viloyat':'Hirot',\
         't-yil':1441,'umr':60}
alloma1={'ism':'temur','familiya':'ibn taragay','viloyat':'Samarqand',\
         't-yil':1336,'umr':65}
alloma2={'ism':'abdulla','familiya':'qodiriy','viloyat':'Toshkent',\
         't-yil':1894,'umr':44}
alloma3={'ism':'erkin','familiya':'vohidov','viloyat':"Farg'ona",\
         't-yil':1936,'umr':80}
allomalar=[alloma0,alloma1,alloma2,alloma3]
#for alloma in allomalar:
#    print(f'{alloma['ism'].title()} {alloma['familiya'].title()}, '
#          f'{alloma['t-yil']}-yilda {alloma['viloyat']}da '
 #         f'tug\'ilgan va {alloma['umr']} yil umr ko\'rgan.')
alloma0['asarlar']=['xamsa','lison ut-tayr','mahbub ul-qulub','mezon ul-avzon',\
        'majolis un-nafois']
alloma1['asarlar']=['temur tuzuklari']
alloma2['asarlar']=["otgan kunlar",'mehrobdan chayon',"obid ketmon"]
alloma3['asarlar']={'tong nafasi','ruhlar isyoni',"inson"}
#for alloma in allomalar:
#    print(f'\n{alloma['ism'].title()} {alloma['familiya'].title()}ning '
#          f'mashhur asarlari:')
#    for asar in alloma['asarlar']:
#       print(f'{asar.title()}',end=', ')
kinolar={'ali':['terminator','tor','hulk2'],\
        'abdulloh':['anime','marvel','superman'],\
        'kamolxon':['black man','beshiktebratar','jumanji']}
#for ism,kinolar in kinolar.items():
#    print(f'\n{ism.title()}ning sevimli kinolari:')
 #   for kino in kinolar:
#        print(kino.title())
davlatlar = {"o'zbekiston":{'poytaxt':'toshkent','hudud':448978,'aholi':38,
             'pul birligi':"so'm"},
             'rossiya':{'poytaxt':'moskva','hudud':17098246,'aholi':145,
                        'pul birligi':'rubl'},
             'amerika':{'poytaxt':'washington CD','hudud':9834000,'aholi':340,
                        'pul birligi':'dollar'},
             'xitoy':{'poytaxt':'pekin','hudud':9597000,'aholi':1.41*1000,
                      'pul birligi':'yuan'}}
davlat=input('Istagan davlatingiz nomini kiriting:').lower()
if davlat in davlatlar.keys():
    info=davlatlar[davlat]
    print(f'\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()} \n'
             f'Hudud {info['hudud']}kv \n'
             f'Aholi soni {info['aholi']}million \n'
             f'Pul birligi {info['pul birligi']}')
else:
         print('Bizda bunday malomot yo\'q')