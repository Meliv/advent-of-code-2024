import day_2 as day, unittest

class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 2)

    def test_part2(self):
        self.assertEqual(day.part_two(), 4)