import unittest
from parameterized import parameterized
import os


class PuzzleDay01:
    @staticmethod
    def solve_puzzle_1(string):
        floor = 0
        for char in string:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            else:
                raise Exception("Incorrect input")
        return floor

    @staticmethod
    def solve_puzzle_2(puzzle_input):
        floor = 0
        for i in range(0, len(puzzle_input)):
            char = puzzle_input[i]
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            else:
                raise Exception("Incorrect input")
            if floor <= -1:
                return i + 1
        raise Exception("Santa never entered the building!")


class TestPuzzleDay01(unittest.TestCase):

    @parameterized.expand([
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ])
    def test_puzzle1_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay01.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 232
        self.assertEqual(puzzle_answer, PuzzleDay01.solve_puzzle_1(puzzle_input))

    @parameterized.expand([
        (")", 1),
        ("()())", 5),
    ])
    def test_puzzle2_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay01.solve_puzzle_2(puzzle_input))

    def test_puzzle2(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 1783
        self.assertEqual(puzzle_answer, PuzzleDay01.solve_puzzle_2(puzzle_input))


if __name__ == '__main__':
    unittest.main()
