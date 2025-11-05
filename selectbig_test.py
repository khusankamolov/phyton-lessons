# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 14:39:59 2025

@author: Surface
"""


import unittest
from selectbig import selectbig

class SelectBigTest(unittest.TestCase):
    def test_selectbig(self):
        self.assertEqual(selectbig(23,43,12),43)
        self.assertEqual(selectbig(21,13,20),21)
        self.assertEqual(selectbig(25,14,72),72)
        self.assertNotEqual(selectbig(19,15,2),15)
        
unittest.main()
    