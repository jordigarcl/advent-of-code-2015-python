import hashlib
import unittest

from parameterized import parameterized


class PuzzleDay04:
    @staticmethod
    def solve_puzzle_1(puzzle_input):
        limit = 10_000_000
        i = 1
        while i < limit:
            md5_hash_input = puzzle_input + str(i)
            md5_hash_hexdigest = hashlib.md5(bytes(md5_hash_input, 'utf-8')).hexdigest()
            if str(md5_hash_hexdigest).startswith("00000"):
                return i
            i += 1
        raise Exception("Limit reached - infinite loop?")

    @staticmethod
    def solve_puzzle_2(puzzle_input):
        limit = 10_000_000
        i = 1
        while i < limit:
            md5_hash_input = puzzle_input + str(i)
            md5_hash_hexdigest = hashlib.md5(bytes(md5_hash_input, 'utf-8')).hexdigest()
            if str(md5_hash_hexdigest).startswith("000000"):
                return i
            i += 1
        raise Exception("Limit reached - infinite loop?")


class TestPuzzleDay04(unittest.TestCase):

    @parameterized.expand([
        ("abcdef", 609043),
        ("pqrstuv", 1048970)
    ])
    def test_puzzle1_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay04.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = "yzbqklnj"
        puzzle_answer = 282749
        self.assertEqual(puzzle_answer, PuzzleDay04.solve_puzzle_1(puzzle_input))

    def test_puzzle2(self):
        puzzle_input = "yzbqklnj"
        puzzle_answer = 9962624
        self.assertEqual(puzzle_answer, PuzzleDay04.solve_puzzle_2(puzzle_input))


if __name__ == '__main__':
    unittest.main()
