#!/usr/bin/python3
# test ase for adding 2 numbers
import unittest

from prog1 import summation

class Testsum(unittest.TestCase):
  def test_list_int(self):
    """
    test case to add 2 nos.
    """
    data=[23,32]
    result=summation(data)
    self.assertEqual(result, 55)
    
if __name__ == '__main__':
  unittest.main()
