# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 11:59:24 2025

@author: Surface
"""

import unittest
from class_main import Shaxs,Talaba

class ShaxsTest(unittest.TestCase):
    
    def setUp(self):
        ism ='Husan'
        familiya='Kamolov'
        passport='F02'
        tyil=2008
        self.shaxs1=Shaxs(ism,familiya,passport,tyil)
        
    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        age=self.shaxs1.get_age(2025)
        self.assertEqual(17,age)
        
    def test_get_info(self):
        shaxs1_info= 'Husan Kamolov. Passport:F02, 2008-yilda tug`ilgan'
        self.assertEqual(shaxs1_info,self.shaxs1.get_info())
    def test_get_age(self):
        self.assertEqual(17,self.shaxs1.get_age(2025))
        
class TalabaTest(unittest.TestCase):
    
    def setUp(self):
        ism="Husan"
        familiya='Kamolov'
        passport='F02'
        tyil=2008
        idraqam='FI12345678'
        bosqich=1
        self.talaba=Talaba(ism,familiya,passport,tyil,idraqam)
    def test_create(self):
        self.assertIsNotNone(self.talaba.ism)
        self.assertIsNotNone(self.talaba.familiya)
        self.assertIsNotNone(self.talaba.passport)
        self.assertIsNotNone(self.talaba.tyil)
        self.assertIsNotNone(self.talaba.idraqam)
        self.assertIsNotNone(self.talaba.bosqich)

    def test_get_info(self):
        
        talaba_info= 'Husan Kamolov. 1-bosqich. ID raqami: FI12345678'
        self.assertEqual(talaba_info,self.talaba.get_info())
    def test_get_id(self):
        self.assertEqual('FI12345678',self.talaba.idraqam)
    def test_get_bosqich(self):
        self.assertEqual(1,self.talaba.bosqich)
    def test_shaxs(self):
        self.assertTrue(isinstance(self.talaba, Shaxs))



    
unittest.main()