import day_1 as day, unittest

class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 11)

    def test_part2(self):
        self.assertEqual(day.part_two(), 31)