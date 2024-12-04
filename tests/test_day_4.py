import day_4 as day, unittest

class TestDay4(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day.part_one(), 18)

    def test_part2(self):
        self.assertEqual(day.part_two(), 0)

    def test_get_diagonal_square(self):
        diag = [
            ['E','F','G','H','I'],
            ['D','E','F','G','H'],
            ['C','D','E','F','G'],
            ['B','C','D','E','F'],
            ['A','B','C','D','E']]
        
        self.assertEqual(''.join(day.get_diagonal(diag)), 'ABBCCCDDDDEEEEEIHHGGGFFFF')
        
    def test_get_diagonal_rectangle_tall(self):
        diag = [
            ['F','G','H'],
            ['E','F','G'],
            ['D','E','F'],
            ['C','D','E'],
            ['B','C','D'],
            ['A','B','C']
        ]
        
        self.assertEqual(''.join(day.get_diagonal(diag)), 'ABBCCCDDDEEEFFFHGG')

    def test_get_diagonal_rectangle_wide(self):
        diag = [
            ['C','D','E','F','G','H','I'],
            ['B','C','D','E','F','G','H'],
            ['A','B','C','D','E','F','G']
        ]
        
        self.assertEqual(''.join(day.get_diagonal(diag)), 'ABBCCCIHHGGGFFFEEEDDD')  
        

