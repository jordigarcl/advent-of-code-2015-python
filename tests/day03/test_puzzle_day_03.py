import unittest
from parameterized import parameterized
import os


class PuzzleDay03:
    @staticmethod
    def solve_puzzle_1(puzzle_input):
        def store_coordinates(visited_coordinates, coordinates):
            visited_coordinates.add((coordinates["x"], coordinates["y"]))

        visited_coordinates = set()
        coordinates = {"x": 0, "y": 0}
        store_coordinates(visited_coordinates, coordinates)

        for char in puzzle_input:
            if char == '^':
                coordinates["y"] += 1
            elif char == 'v':
                coordinates["y"] -= 1
            elif char == '>':
                coordinates["x"] += 1
            elif char == '<':
                coordinates["x"] -= 1
            else:
                raise Exception("Unknown direction: " + char)
            store_coordinates(visited_coordinates, coordinates)

        return len(visited_coordinates)

    @staticmethod
    def solve_puzzle_2(puzzle_input):
        def store_coordinates(visited_coordinates, coordinates):
            visited_coordinates.add((coordinates["x"], coordinates["y"]))

        visited_coordinates = set()
        coordinates_santa = {"x": 0, "y": 0}
        coordinates_robosanta = {"x": 0, "y": 0}
        store_coordinates(visited_coordinates, coordinates_santa)

        is_santas_turn = True
        for char in puzzle_input:
            coordinates = coordinates_santa if is_santas_turn else coordinates_robosanta
            if char == '^':
                coordinates["y"] += 1
            elif char == 'v':
                coordinates["y"] -= 1
            elif char == '>':
                coordinates["x"] += 1
            elif char == '<':
                coordinates["x"] -= 1
            else:
                raise Exception("Unknown direction: " + char)
            store_coordinates(visited_coordinates, coordinates)
            is_santas_turn = not is_santas_turn

        return len(visited_coordinates)


class TestPuzzleDay03(unittest.TestCase):

    @parameterized.expand([
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ])
    def test_puzzle1_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay03.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 2592
        self.assertEqual(puzzle_answer, PuzzleDay03.solve_puzzle_1(puzzle_input))

    @parameterized.expand([
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11)
    ])
    def test_puzzle2_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay03.solve_puzzle_2(puzzle_input))

    def test_puzzle2(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 2360
        self.assertEqual(puzzle_answer, PuzzleDay03.solve_puzzle_2(puzzle_input))


if __name__ == '__main__':
    unittest.main()
