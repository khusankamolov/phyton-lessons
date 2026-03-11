# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 15:00:39 2025

@author: Surface
"""

import unittest 
from texttitle import texttitle

class TextTitleTest(unittest.TestCase):
    def test_text(self):
        self.assertIn("Hasan", texttitle())
        self.assertIn('Shohrux',texttitle())
        self.assertIn('Akbar',texttitle())
        self.assertNotIn('bahodir',texttitle())
        self.assertIn('Salohiddin',texttitle())

unittest.main()