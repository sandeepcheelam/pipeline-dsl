'''
Created on Mar 20, 2018

@author: rajesred
'''
import unittest
from demo import Prime

class PrimesTestCase(unittest.TestCase):
  """Tests for `primes.py`."""

  def setUp(self):
    self.prime = Prime()

  def tearDown(self):
    unittest.TestCase.tearDown(self)
    self.prime = None

  def test_is_five_prime(self):
    """Is five successfully determined to be prime?"""
    self.assertTrue(self.prime.is_prime(5))

if __name__ == '__main__':
  unittest.main()
