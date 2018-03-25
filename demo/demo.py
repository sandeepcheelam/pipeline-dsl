'''
Created on Mar 20, 2018

@author: rajesred
'''

class Prime(object):
  '''
  This will verify prime
  '''
  def __init__(self):
    '''
    '''
    pass

  def is_prime(self, number):
    """Return True if *number* is prime."""
    for element in range(2, number):
      if number % element == 0:
        return False

    return True

def print_next_prime(self, number):
  """Print the closest prime number larger than *number*."""
  index = number
  while True:
    index += 1
    if self.is_prime(index):
      print(index)

