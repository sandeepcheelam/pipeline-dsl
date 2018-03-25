'''
:Author: Rajeshkumar Reddy
:Contact: rajesred@cisco.com, paas-team@cisco.com
:Updated: June 21, 2017
'''

import os
import sys
import unittest
from setuptools import setup

def discover_tests():
  """ discover tests"""
  file_patterns = ['*_unit_tests.py']
  setup_file = sys.modules['__main__'].__file__
  setup_dir = os.path.abspath(os.path.dirname(setup_file))
  tests_dir = os.path.join(setup_dir, 'tests')
  test_suite = unittest.TestSuite(tests=())
  for pattern in file_patterns:
    tests = unittest.defaultTestLoader.discover(tests_dir, pattern)
    test_suite.addTests(tests)
  return test_suite

setup(
  name='demo',
  version='0.0.1',
  description='Pipeline dsl demo',
  author='Rajesh Reddy',
  author_email='rajesred@cisco.com',
  url='http://gitscm.cisco.com/scm/paas/pipeline-dsl.git',
  packages=['demo'],
  scripts=[],
  data_files=[],
  install_requires=[],
)
