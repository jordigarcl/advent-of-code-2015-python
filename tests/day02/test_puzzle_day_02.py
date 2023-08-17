import unittest
from parameterized import parameterized


class PuzzleDay02:
    @staticmethod
    def solve_puzzle_1(puzzle_input):
        def inner(puzzle_input):
            for line in puzzle_input.splitlines():
                length, width, height = [int(number) for number in line.split('x')]
                area_a, area_b, area_c = (length * width), (width * height), (height * length)
                yield 2 * area_a + 2 * area_b + 2 * area_c + min(area_a, area_b, area_c)

        return sum(list(inner(puzzle_input)))


class TestPuzzleDay02(unittest.TestCase):

    @parameterized.expand([
        ("2x3x4", 58),
        ("1x1x10", 43),
        ("2x3x4\n1x1x10", 58 + 43),
    ])
    def test_puzzle1_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay02.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = open("input_puzzle1.txt", "r").read()
        puzzle_answer = 232
        self.assertEqual(puzzle_answer, PuzzleDay02.solve_puzzle_1(puzzle_input))


if __name__ == '__main__':
    unittest.main()
