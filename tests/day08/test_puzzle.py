import unittest
import os


class PuzzleDay08:

    @staticmethod
    def solve_puzzle_1(puzzle_input):

        def process_lines(lines):
            for line in lines:
                decoded_string = bytes(line, "utf-8").decode("unicode_escape")
                print(f'{line} -> {decoded_string}')
                yield len(line) - (len(decoded_string) - 2)

        return sum(list(process_lines(puzzle_input.splitlines())))

    @staticmethod
    def solve_puzzle_2(puzzle_input):

        def process_lines(lines):
            for line in lines:
                encoded_string = line.encode("unicode_escape").decode('utf-8').replace("\"", "\\\"")
                print(f'{line} -> {encoded_string}')
                yield (len(encoded_string) + 2) - len(line)

        return sum(list(process_lines(puzzle_input.splitlines())))


class TestPuzzleDay06(unittest.TestCase):

    def test_puzzle1_examples(self):
        puzzle_input = """\"\"
\"abc\"
\"aaa\\\"aaa"
\"\\x27\""""
        puzzle_solution = 12
        self.assertEqual(puzzle_solution, PuzzleDay08.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 1350
        self.assertEqual(puzzle_answer, PuzzleDay08.solve_puzzle_1(puzzle_input))

    def test_puzzle2_examples(self):
        puzzle_input = """\"\"
\"abc\"
\"aaa\\\"aaa"
\"\\x27\""""
        puzzle_solution = 19
        self.assertEqual(puzzle_solution, PuzzleDay08.solve_puzzle_2(puzzle_input))

    def test_puzzle2(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 2085
        self.assertEqual(puzzle_answer, PuzzleDay08.solve_puzzle_2(puzzle_input))


if __name__ == '__main__':
    unittest.main()
