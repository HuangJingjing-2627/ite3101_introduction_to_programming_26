import unittest 
from tests.unit_test_helper.console_tset_helper import *


class Test0utput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t09_numbers.py")
        print(temp_locals)
        self.assertAlmostEqual(1, temp_locals{})