import unittest

from day3 import Route, IntersectionFinder

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([(1,0),(2,0),(3,0)], Route("R3").get_coords())
        self.assertEqual([(1,0),(2,0),(3,0),(2,0),(1,0)], Route("R3,L2").get_coords())

    def test_find_shortest_manhattan_distance(self):
        route1 = Route("R8,U5,L5,D3")
        route2 = Route("U7,R6,D4,L4")
        manhattan = IntersectionFinder([route1, route2]).find_shortest_manhattan_distance()
        self.assertEqual(6, manhattan)

    def test_find_shortest_signal_delay(self):
        route1 = Route("R75,D30,R83,U83,L12,D49,R71,U7,L72")
        route2 = Route("U62,R66,U55,R34,D71,R55,D58,R83")
        signalDelay = IntersectionFinder([route1, route2]).find_shortest_signal_delay()
        self.assertEqual(610, signalDelay)

    def test_find_shortest_signal_delay_2(self):
        route1 = Route("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        route2 = Route("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        signalDelay = IntersectionFinder([route1, route2]).find_shortest_signal_delay()
        self.assertEqual(410, signalDelay)

if __name__ == '__main__':
    unittest.main()
