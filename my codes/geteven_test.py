# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 15:30:27 2025

@author: Surface
"""

import unittest 
from geteven import get_even
class GetEvenTest(unittest.TestCase):
    
    def test_geteven(self):
        self.assertIn(12,get_even())
        self.assertIn(66,get_even())
        self.assertIn(68,get_even())
        self.assertNotIn(14,get_even())
        
unittest.main()