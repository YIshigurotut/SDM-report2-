#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample5 (self):
                self.assertEqual (-1, calc(-1,-1)) 

        def test_sample6 (self):
                self.assertEqual (-1, calc(0,0)) 
        
        def test_sample7 (self):
                self.assertEqual (-1, calc(0.9,0.9)) 
        
        def test_sample8 (self):
                self.assertEqual (1, calc(1,1)) 
        
        def test_sample9 (self):
                self.assertEqual (10000, calc(100,100)) 
        
        def test_sample10 (self):
                self.assertEqual (-1, calc(100.5,100.5)) 
        
        def test_sample11 (self):
                self.assertEqual (998001, calc(999,999)) 

        def test_sample12 (self):
                self.assertEqual (-1, calc(999.1,999.1)) 

        def test_sample13 (self):
                self.assertEqual (-1, calc(1000,1000)) 

        def test_sample14 (self):
                self.assertEqual (-1, calc(-1,100))

        def test_sample15 (self):
                self.assertEqual (-1, calc(100.5,100))

        def test_sample16 (self):
                self.assertEqual (-1, calc(999.1,100))

        def test_sample17 (self):
                self.assertEqual (-1, calc(100,1000))    

        def test_sample18 (self):
                self.assertEqual (-1, calc('a',100)) 

