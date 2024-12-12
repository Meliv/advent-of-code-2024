import day_12 as day, unittest

class TestDay12(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 1930)

    def test_part2(self):
        self.assertEqual(day.part_two(), 0)