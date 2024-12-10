import day_10 as day, unittest

class TestDay10(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 36)

    def test_part2(self):
        self.assertEqual(day.part_two(), 81)