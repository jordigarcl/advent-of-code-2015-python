import os
import unittest

from parameterized import parameterized


class PuzzleDay05:
    @staticmethod
    def solve_puzzle_1(puzzle_input):
        def inner(line):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            num_vowels = 0

            previous_char = None
            a_char_was_repeated = False

            prohibited_strings = {"ab", "cd", "pq", "xy"}

            for i in range(len(line)):
                current_char = line[i]
                if num_vowels < 3 and current_char in vowels:
                    num_vowels += 1
                if not a_char_was_repeated and current_char == previous_char:
                    a_char_was_repeated = True
                if i > 0 and line[i - 1:i + 1] in prohibited_strings:
                    return False

                previous_char = current_char

            return num_vowels >= 3 and a_char_was_repeated

        return sum(1 for line in puzzle_input.splitlines() if inner(line))

    @staticmethod
    def solve_puzzle_2(puzzle_input):
        def inner(line):
            if len(line) < 4:
                return False

            a_char_was_repeated_with_letter_between_them = False
            a_pair_of_two_chars_appear_twice_without_overlapping = False
            char_pairs = []

            for i in range(len(line)):
                if i >= 2 and not a_char_was_repeated_with_letter_between_them and line[i] == line[i - 2]:
                    a_char_was_repeated_with_letter_between_them = True

                if i >= 3:
                    try:
                        char_pairs.index(line[i - 1:i + 1], 0, len(char_pairs) - 1)
                        a_pair_of_two_chars_appear_twice_without_overlapping = True
                    except ValueError:
                        pass

                if i >= 1:
                    char_pairs.append(line[i - 1:i + 1])

            return a_char_was_repeated_with_letter_between_them and a_pair_of_two_chars_appear_twice_without_overlapping

        return sum(1 for line in puzzle_input.splitlines() if inner(line))


class TestPuzzleDay05(unittest.TestCase):

    @parameterized.expand([
        ("ugknbfddgicrmopn", 1),
        ("aaa", 1),
        ("jchzalrnumimnmhp", 0),
        ("haegwjzuvuyypxyu", 0),
        ("dvszwmarrgswjxmb", 0),
    ])
    def test_puzzle1_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay05.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 238
        self.assertEqual(puzzle_answer, PuzzleDay05.solve_puzzle_1(puzzle_input))

    @parameterized.expand([
        ("qjhvhtzxzqqjkmpb", 1),
        ("xxyxx", 1),
        ("uurcxstgmygtbstg", 0),
        ("ieodomkazucvgmuy", 0),
    ])
    def test_puzzle2_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay05.solve_puzzle_2(puzzle_input))

    def test_puzzle2(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 69
        self.assertEqual(puzzle_answer, PuzzleDay05.solve_puzzle_2(puzzle_input))


if __name__ == '__main__':
    unittest.main()
