import unittest

from my_sum import sum

import fractions

from fractions import Fraction

import decimal 

from decimal import Decimal

from decimal import getcontext

getcontext().prec = 1
 
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
 
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]
        result = sum(data)
        self.assertEqual(result, 1)
    
    def test_list_decimal(self):
        """
        Test that it can sum a list of decimals
        """
        data = [Decimal(1.1), Decimal(2.2), Decimal(3.2)]
        result = sum(data)
        self.assertEqual(result, 6.5)
       
if __name__ == '__main__':
    unittest.main()
