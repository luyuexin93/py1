import unittest
import requests

class testadd(unittest.TestCase):
    def setUp(self):
        pass
    def test_add1(self):
         self.assertEqual(2+3+5,10)
    def test_add2(self):
         self.assertEqual(0+8+7,15)
    def tearDown(self):
         pass