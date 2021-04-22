import unittest
from solution.algorithms.utils import *

class TestUtils(unittest.TestCase):

    def test_validate_grid_empty(self):
        n='3'
        grid_empty= '[\'---\',\'---\',\'---\']'

        false_result = validate_grid(n, grid_empty)
        self.assertEqual(false_result,False)

    def test_validate_grid_true(self):
        n='3'
        grid_correct_format = '[\'m--\',\'-x-\',\'-p-\']'

        true_result = validate_grid(n, grid_correct_format)
        self.assertEqual(true_result,True)

    def test_validate_grid_only_mario(self):
        n='3'
        grid_one_mario = '[\'---\',\'---\',\'-m-\']'

        false_result = validate_grid(n, grid_one_mario)
        self.assertEqual(false_result,False)
    
    def test_validate_multiple(self):
        n='3'
        grid_two_mario = '[\'-m-\',\'---\',\'-m-\']'
        grid_two_princess = '[\'-p-\',\'---\',\'-p-\']'

        false_result = validate_grid(n, grid_two_mario)
        false_result1 = validate_grid(n, grid_two_princess)
        self.assertEqual(false_result,False)
        self.assertEqual(false_result1,False)

    def test_find_mario_position(self):
        matrix_test = ['-m-','-p-','---']
        mario_correct_position = (0,1)

        matrix_test1 = ['-p-','-m-','---']
        mario_correct_position1 = (1,1)

        no_mario_matrix = ['-p-','---','---']
        mario_correct_position2 = None

        returned_position = find_marion_position(matrix_test)
        returned_position1 = find_marion_position(matrix_test1)
        returned_position2 = find_marion_position(no_mario_matrix)

        self.assertEqual(returned_position,mario_correct_position)
        self.assertEqual(returned_position1,mario_correct_position1)
        self.assertEqual(returned_position2,mario_correct_position2)

    


        

