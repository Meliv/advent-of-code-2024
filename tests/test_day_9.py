import day_9 as day, unittest

class TestDay9(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 1928)

    def test_part2(self):
        self.assertEqual(day.part_two(), 0)