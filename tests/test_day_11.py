import day_11 as day, unittest

class TestDay11(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 55312)

    def test_part2(self):
        self.assertEqual(day.part_two(), 0)