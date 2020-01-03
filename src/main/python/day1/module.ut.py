import unittest

from day2 import Module, FuelCounterUpper

class ModuleTestCase(unittest.TestCase):
    def test_fuel_calculation(self):
        self.assertEqual(2, Module(12).calculate_fuel_needed())
        self.assertEqual(2, Module(14).calculate_fuel_needed())
        self.assertEqual(654, Module(1969).calculate_fuel_needed())
        self.assertEqual(33583, Module(100756).calculate_fuel_needed())

    def test_fuel_for_fuel_calculation(self):
        module = Module(1969)
        self.assertEqual(966, module.calculate_fuel_needed() + module.calculate_fuel_for_fuel())
        module = Module(100756)
        self.assertEqual(50346, module.calculate_fuel_needed() + module.calculate_fuel_for_fuel())

class FuelCounterUpperTestCase(unittest.TestCase):
    def test_total_fuel(self):
        self.assertEqual(1308, FuelCounterUpper('../../resources/day1/test-input.txt').calculate_total_fuel_required())

    def test_fuel_for_fuel(self):
        self.assertEqual(624, FuelCounterUpper('../../resources/day1/test-input.txt').calculate_total_fuel_required_for_fuel())

if __name__ == '__main__':
    unittest.main()
