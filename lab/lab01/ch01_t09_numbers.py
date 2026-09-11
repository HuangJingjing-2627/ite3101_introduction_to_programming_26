import unittest 
from tests.unit_test_helper.console_tset_helper import *


class Test0utput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t09_numbers.py")
        print(temp_locals)
        self.assertAlmostEqual(1, temp_locals{'cucumbers'})
        self.assertAlmostEqual(3.25, temp_locals{'price_per_cucumber'})
        self.assertAlmostEqual(3.25, temp_locals{'total_cost'})


if __name__ == '__main__':
    