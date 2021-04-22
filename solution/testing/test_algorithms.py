import unittest
from solution.algorithms.algorithms import *

class TestAlgorithms(unittest.TestCase):

    def test_find_princess(self):
        grid = ['-m-','-x-','--p']
        grid1 = ['--m','-x-','--p']
        grid2 = ['p---','-xxx','----','--mx-']
        n = 3
        n1 = 4
        start_row = 0
        start_column = 1

        start_row1 = 0
        start_column1 = 2

        start_row2 = 3
        start_column2 = 2

        path_to_p =  ['RIGHT','DOWN','DOWN']
        path_to_p1 = ['DOWN','DOWN']
        path_to_p2 = ['UP','LEFT','LEFT','UP','UP']

        returned_path = find_princess(grid,n,start_row,start_column)
        returned_path1 = find_princess(grid1,n,start_row1,start_column1)
        returned_path2 = find_princess(grid2,n1,start_row2,start_column2)

        self.assertEqual(returned_path,path_to_p)
        self.assertEqual(returned_path1,path_to_p1)
        self.assertEqual(returned_path2,path_to_p2)


