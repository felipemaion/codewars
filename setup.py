import unittest
import datetime


class Test(unittest.TestCase):
    def __init__(self):
        self.data = []

    def describe(test_desc, *arg):
        print (test_desc, *arg)
    def it(desc):
        print(desc)
    def assert_equals(one, two, msg=None):
        #print(one, ' == ', two)
        unittest.TestCase().assertEqual(one, two, msg=None)
    def assert_not_equals(one, two, msg=None):
        unittest.TestCase().assertNotEqual(one, two, msg=None)

test = Test

def xrange(*att):
    return range(*att)

# Todo:
# Implementar metaprogramming para criar as def conforme iniciar o Test.describe(txt) e rodar o
# Test.assert_equals em cima de um def test_*describe*
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Metaprogramming.html

def comment(desc_program=""):
    print ("###############################################")
    print(desc_program)
