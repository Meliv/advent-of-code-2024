import day_7 as day, unittest

class TestDay7(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 3749)

    def test_part2(self):
        self.assertEqual(day.part_two(), 11387)