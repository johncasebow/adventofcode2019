import unittest

from day2 import IntcodeComputer

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([2,0,0,0,99], IntcodeComputer([1,0,0,0,99]).run_program())
        self.assertEqual([2,3,0,6,99], IntcodeComputer([2,3,0,3,99]).run_program())
        self.assertEqual([30,1,1,4,2,5,6,0,99], IntcodeComputer([1,1,1,4,99,5,6,0,99]).run_program())

if __name__ == '__main__':
    unittest.main()
