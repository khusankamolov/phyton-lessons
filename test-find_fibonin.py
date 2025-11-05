# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 16:10:55 2025

@author: Surface
"""

import unittest
from find_fiboninchi import find_fibonin

class FiboninchiTest(unittest.TestCase):
    
    def test_find_fibonin(self):
       """This function check number whether is in fiboninchi list(to 1000)"""
       self.assertFalse(find_fibonin(76))
       self.assertTrue(find_fibonin(34))
       self.assertTrue(find_fibonin(21))
       self.assertTrue(find_fibonin(8))
       self.assertTrue(find_fibonin(55))
       self.assertFalse(find_fibonin(37))

       
unittest.main()



       