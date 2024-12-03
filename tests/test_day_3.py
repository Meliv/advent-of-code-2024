import day_3 as day, unittest

class TestDay3(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 161)

    def test_part2(self):
        self.assertEqual(day.part_two(), 48)