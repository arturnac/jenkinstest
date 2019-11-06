import unittest

from main import *

class TestMain(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(TestMain, self).__init__(methodName)

    def setUp(self):
        self.a = 5
        self.b = 2
        self.results_sum = [7, 6, 8, 43, 0]
        self.results_sub = [3, 6, 8, 43, 0]
        self.results_mul = [10, 6, 8, 43, 0]
        self.results_div = [2.5, 6, 8, 43, 0]

    def tearDown(self):
        pass

    def test_sum(self):
        total = sum(self.a, self.b)
        self.assertEqual(self.results_sum[0], total)
        for result in self.results_sum[1:]:
            self.assertNotEqual(result, total)
    
    def test_sub(self):
        total = sub(self.a, self.b)
        self.assertEqual(self.results_sub[0], total)
        for result in self.results_sub[1:]:
            self.assertNotEqual(result, total)
    
    def test_mul(self):
        total = mul(self.a, self.b)
        self.assertEqual(self.results_mul[0], total)
        for result in self.results_mul[1:]:
            self.assertNotEqual(result, total)
    
    def test_div(self):
        total = div(self.a, self.b)
        self.assertEqual(self.results_div[0], total)
        for result in self.results_div[1:]:
            self.assertNotEqual(result, total)
    
    def test_is_even(self):
        self.assertNotEqual(True, is_even(self.a))
        self.assertEqual(True, is_even(self.b))