import math


class Module:

    def __init__(self, mass=0):
        self.mass = mass

    def calculate_fuel_needed(self):
        fuel = math.floor(self.mass / 3) - 2
        return fuel

    def calculate_fuel_for_fuel(self):
        total = 0;
        fuelForFuel = Module(self.calculate_fuel_needed()).calculate_fuel_needed()
        while fuelForFuel > 0:
            total += fuelForFuel
            fuelForFuel = Module(fuelForFuel).calculate_fuel_needed()

        return total


class FuelCounterUpper:

    def __init__(self, filename=""):
        self.modules = []
        file = open(filename, 'r')
        for line in file:
            mass = int(line)
            self.modules.append(Module(mass))
        file.close()

    def calculate_total_fuel_required(self):
        totalFuel = 0
        for module in self.modules:
            totalFuel += module.calculate_fuel_needed()
        return totalFuel

    def calculate_total_fuel_required_for_fuel(self):
        totalFuel = 0
        for module in self.modules:
            totalFuel += module.calculate_fuel_for_fuel()
        return totalFuel



if __name__ == '__main__':
    counterUpper = FuelCounterUpper("../../resources/day1/input.txt")
    fuelForMass = counterUpper.calculate_total_fuel_required()
    fuelForFuel = counterUpper.calculate_total_fuel_required_for_fuel()
    total = fuelForMass + fuelForFuel
    print("Total fuel required: " + str(total))