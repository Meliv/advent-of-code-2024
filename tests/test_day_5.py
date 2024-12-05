import day_5 as day, unittest

class TestDay5(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 143)

    def test_part2(self):
        self.assertEqual(day.part_two(), 0)