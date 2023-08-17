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

    @staticmethod
    def solve_puzzle_2(puzzle_input):
        def inner(puzzle_input):
            for line in puzzle_input.splitlines():
                length, width, height = [int(number) for number in line.split('x')]

                wrapping_ribbon = min(2 * (length + width), 2 * (width + height), 2 * (height + length))
                bow_ribbon = length * width * height
                yield wrapping_ribbon + bow_ribbon

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
        puzzle_input = open("input_puzzle.txt", "r").read()
        puzzle_answer = 1588178
        self.assertEqual(puzzle_answer, PuzzleDay02.solve_puzzle_1(puzzle_input))

    @parameterized.expand([
        ("2x3x4", 34),
        ("1x1x10", 14)
    ])
    def test_puzzle2_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay02.solve_puzzle_2(puzzle_input))

    def test_puzzle2(self):
        puzzle_input = open("input_puzzle.txt", "r").read()
        puzzle_answer = 3783758
        self.assertEqual(puzzle_answer, PuzzleDay02.solve_puzzle_2(puzzle_input))



if __name__ == '__main__':
    unittest.main()
