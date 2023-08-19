import os
import re
import unittest

from parameterized import parameterized


class PuzzleDay06:
    @staticmethod
    def solve_puzzle_1(puzzle_input):
        x_max = 1000
        y_max = 1000
        grid = [False for _ in range(x_max * y_max)]

        def line_parser(line):
            regex = r'(\w+\s*\w+)\s(\d+,\d+)\sthrough\s(\d+,\d+)'
            match = re.match(regex, line)

            # e.g. 'turn off 499,499 through 500,500'
            instruction = match.group(1)  # e.g. "turn off"
            start = match.group(2)  # e.g. "499,499"
            end = match.group(3)  # e.g. "500,500"

            return {
                "instruction": instruction,
                "coordinate_1": {
                    "x": int(start.split(",")[0]),
                    "y": int(start.split(",")[1])
                },
                "coordinate_2": {
                    "x": int(end.split(",")[0]),
                    "y": int(end.split(",")[1])
                },
            }

        def resolve_index(x, y):
            return x + y_max * y

        def process_line(line):
            parsed_line = line_parser(line)

            instruction = parsed_line["instruction"]
            max_x_local = max(parsed_line["coordinate_1"]["x"], parsed_line["coordinate_2"]["x"])
            max_y_local = max(parsed_line["coordinate_1"]["y"], parsed_line["coordinate_2"]["y"])
            min_x_local = min(parsed_line["coordinate_1"]["x"], parsed_line["coordinate_2"]["x"])
            min_y_local = min(parsed_line["coordinate_1"]["y"], parsed_line["coordinate_2"]["y"])

            pos_x, pos_y = min_x_local, min_y_local
            finished = False
            while not finished:
                index = resolve_index(pos_x, pos_y)
                if instruction == "turn on":
                    grid[index] = True
                if instruction == "turn off":
                    grid[index] = False
                if instruction == "toggle":
                    grid[index] = not grid[index]

                if pos_x == max_x_local and pos_y == max_y_local:
                    finished = True
                else:
                    pos_x += 1
                    if pos_x > max_x_local:
                        pos_x = min_x_local
                        pos_y += 1

        for line in puzzle_input.splitlines():
            process_line(line)

        return sum(1 for light_is_on in grid if light_is_on)

    @staticmethod
    def solve_puzzle_2(puzzle_input):
        x_max = 1000
        y_max = 1000
        grid = [0 for _ in range(x_max * y_max)]

        def line_parser(line):
            regex = r'(\w+\s*\w+)\s(\d+,\d+)\sthrough\s(\d+,\d+)'
            match = re.match(regex, line)

            # e.g. 'turn off 499,499 through 500,500'
            instruction = match.group(1)  # e.g. "turn off"
            start = match.group(2)  # e.g. "499,499"
            end = match.group(3)  # e.g. "500,500"

            return {
                "instruction": instruction,
                "coordinate_1": {
                    "x": int(start.split(",")[0]),
                    "y": int(start.split(",")[1])
                },
                "coordinate_2": {
                    "x": int(end.split(",")[0]),
                    "y": int(end.split(",")[1])
                },
            }

        def resolve_index(x, y):
            return x + y_max * y

        def process_line(line):
            parsed_line = line_parser(line)

            instruction = parsed_line["instruction"]
            max_x_local = max(parsed_line["coordinate_1"]["x"], parsed_line["coordinate_2"]["x"])
            max_y_local = max(parsed_line["coordinate_1"]["y"], parsed_line["coordinate_2"]["y"])
            min_x_local = min(parsed_line["coordinate_1"]["x"], parsed_line["coordinate_2"]["x"])
            min_y_local = min(parsed_line["coordinate_1"]["y"], parsed_line["coordinate_2"]["y"])

            pos_x, pos_y = min_x_local, min_y_local
            finished = False
            while not finished:
                index = resolve_index(pos_x, pos_y)
                if instruction == "turn on":
                    grid[index] += 1
                if instruction == "turn off":
                    if grid[index] > 0:
                        grid[index] -= 1
                if instruction == "toggle":
                    grid[index] += 2

                if pos_x == max_x_local and pos_y == max_y_local:
                    finished = True
                else:
                    pos_x += 1
                    if pos_x > max_x_local:
                        pos_x = min_x_local
                        pos_y += 1

        for line in puzzle_input.splitlines():
            process_line(line)

        return sum(light_is_on for light_is_on in grid)



class TestPuzzleDay06(unittest.TestCase):

    @parameterized.expand([
        ("turn on 0,0 through 999,999", 1000 * 1000),
        ("toggle 0,0 through 999,0", 1000)
    ])
    def test_puzzle1_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay06.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 543903
        self.assertEqual(puzzle_answer, PuzzleDay06.solve_puzzle_1(puzzle_input))

    @parameterized.expand([
        ("turn on 0,0 through 0,0", 1),
        ("toggle 0,0 through 999,999", 2000000)
    ])
    def test_puzzle2_examples(self, puzzle_input, puzzle_solution):
        self.assertEqual(puzzle_solution, PuzzleDay06.solve_puzzle_2(puzzle_input))

    def test_puzzle2(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 14687245
        self.assertEqual(puzzle_answer, PuzzleDay06.solve_puzzle_2(puzzle_input))


if __name__ == '__main__':
    unittest.main()
