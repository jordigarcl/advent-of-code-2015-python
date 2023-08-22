import os
import re
import unittest

from parameterized import parameterized


class PuzzleDay06:

    @staticmethod
    def solve_puzzle_1(puzzle_input, target_gate):
        mask16 = 0xFFFF

        class Gate:
            def __init__(self, kind, name, inputs):
                self.kind = kind
                self.name = name
                self.inputs = inputs
                self.output = None

            def resolve_value(self, input):
                if input.isnumeric():
                    return int(input) & mask16
                else:
                    return circuit.get_gate(input).resolve_output()

            def resolve_output(self):
                if self.output is not None:
                    return self.output

                print(f"❓ Resolving {self.name}...")

                if self.kind == "NOT":
                    val1 = self.resolve_value(self.inputs[0])
                    self.output = (~val1) & mask16
                elif self.kind == "AND":
                    val1 = self.resolve_value(self.inputs[0])
                    val2 = self.resolve_value(self.inputs[1])
                    self.output = (val1 & val2) & mask16
                elif self.kind == "OR":
                    val1 = self.resolve_value(self.inputs[0])
                    val2 = self.resolve_value(self.inputs[1])
                    self.output = (val1 | val2) & mask16
                elif self.kind == "LSHIFT":
                    val1 = self.resolve_value(self.inputs[0])
                    val2 = self.resolve_value(self.inputs[1])
                    self.output = (val1 << val2) & mask16
                elif self.kind == "RSHIFT":
                    val1 = self.resolve_value(self.inputs[0])
                    val2 = self.resolve_value(self.inputs[1])
                    self.output = (val1 >> val2) & mask16
                elif self.kind == "DIRECT":
                    val1 = self.resolve_value(self.inputs[0])
                    self.output = (val1) & mask16
                else:
                    raise Exception("this should not happen")

                print(f"✅ Resolved {self.name}: {self.output}")
                return self.output

        class Circuit:
            def __init__(self, gates):
                self.gates = dict()
                for gate in gates:
                    self.gates[gate.name] = gate

            def get_gate(self, gate_name):
                return self.gates[gate_name]

        def parse_gates(puzzle_input):
            regex_not = r'NOT (\w+) -> (\w+)'
            regex_and = r'(\w+) AND (\w+) -> (\w+)'
            regex_or = r'(\w+) OR (\w+) -> (\w+)'
            regex_lshift = r'(\w+) LSHIFT (\w+) -> (\w+)'
            regex_rshift = r'(\w+) RSHIFT (\w+) -> (\w+)'
            regex_direct = r'(\w+) -> (\w+)'

            for line in puzzle_input.splitlines():
                match = re.match(regex_not, line)
                if match is not None:
                    # e.g. "NOT x -> h"
                    input_1 = match.group(1)  # e.g. "x"
                    output = match.group(2)  # e.g. "h"
                    yield Gate("NOT", output, [input_1])

                match = re.match(regex_and, line)
                if match is not None:
                    # e.g. "x AND y -> d"
                    input_1 = match.group(1)  # e.g. "x"
                    input_2 = match.group(2)  # e.g. "y"
                    output = match.group(3)  # e.g. "d"
                    yield Gate("AND", output, [input_1, input_2])

                match = re.match(regex_or, line)
                if match is not None:
                    # e.g. "x OR y -> e"
                    input_1 = match.group(1)  # e.g. "x"
                    input_2 = match.group(2)  # e.g. "y"
                    output = match.group(3)  # e.g. "e"
                    yield Gate("OR", output, [input_1, input_2])

                match = re.match(regex_lshift, line)
                if match is not None:
                    # e.g. "x LSHIFT 2 -> f"
                    input_1 = match.group(1)  # e.g. "x"
                    input_2 = match.group(2)  # e.g. "2"
                    output = match.group(3)  # e.g. "f"
                    yield Gate("LSHIFT", output, [input_1, input_2])

                match = re.match(regex_rshift, line)
                if match is not None:
                    # e.g. "x RSHIFT 2 -> f"
                    input_1 = match.group(1)  # e.g. "x"
                    input_2 = match.group(2)  # e.g. "2"
                    output = match.group(3)  # e.g. "f"
                    yield Gate("RSHIFT", output, [input_1, input_2])

                match = re.match(regex_direct, line)
                if match is not None:
                    # e.g. "123 -> x"
                    input_1 = match.group(1)  # e.g. "123"
                    output = match.group(2)  # e.g. "x"
                    yield Gate("DIRECT", output, [input_1])

        # === start of main ===
        circuit = Circuit(parse_gates(puzzle_input))
        return circuit.get_gate(target_gate).resolve_output()

    # @staticmethod
    # def solve_puzzle_2(puzzle_input):
    #     x_max = 1000
    #     y_max = 1000
    #     grid = [0 for _ in range(x_max * y_max)]
    #
    #     def line_parser(line):
    #         regex = r'(\w+\s*\w+)\s(\d+,\d+)\sthrough\s(\d+,\d+)'
    #         match = re.match(regex, line)
    #
    #         # e.g. 'turn off 499,499 through 500,500'
    #         instruction = match.group(1)  # e.g. "turn off"
    #         start = match.group(2)  # e.g. "499,499"
    #         end = match.group(3)  # e.g. "500,500"
    #
    #         return {
    #             "instruction": instruction,
    #             "coordinate_1": {
    #                 "x": int(start.split(",")[0]),
    #                 "y": int(start.split(",")[1])
    #             },
    #             "coordinate_2": {
    #                 "x": int(end.split(",")[0]),
    #                 "y": int(end.split(",")[1])
    #             },
    #         }
    #
    #     def resolve_index(x, y):
    #         return x + y_max * y
    #
    #     def process_line(line):
    #         parsed_line = line_parser(line)
    #
    #         instruction = parsed_line["instruction"]
    #         max_x_local = max(parsed_line["coordinate_1"]["x"], parsed_line["coordinate_2"]["x"])
    #         max_y_local = max(parsed_line["coordinate_1"]["y"], parsed_line["coordinate_2"]["y"])
    #         min_x_local = min(parsed_line["coordinate_1"]["x"], parsed_line["coordinate_2"]["x"])
    #         min_y_local = min(parsed_line["coordinate_1"]["y"], parsed_line["coordinate_2"]["y"])
    #
    #         pos_x, pos_y = min_x_local, min_y_local
    #         finished = False
    #         while not finished:
    #             index = resolve_index(pos_x, pos_y)
    #             if instruction == "turn on":
    #                 grid[index] += 1
    #             if instruction == "turn off":
    #                 if grid[index] > 0:
    #                     grid[index] -= 1
    #             if instruction == "toggle":
    #                 grid[index] += 2
    #
    #             if pos_x == max_x_local and pos_y == max_y_local:
    #                 finished = True
    #             else:
    #                 pos_x += 1
    #                 if pos_x > max_x_local:
    #                     pos_x = min_x_local
    #                     pos_y += 1
    #
    #     for line in puzzle_input.splitlines():
    #         process_line(line)
    #
    #     return sum(light_is_on for light_is_on in grid)


class TestPuzzleDay06(unittest.TestCase):

    @parameterized.expand([
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("x", 123),
        ("y", 456),
    ])
    def test_puzzle1_examples(self, target_date, puzzle_solution):
        puzzle_input = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

        self.assertEqual(puzzle_solution, PuzzleDay06.solve_puzzle_1(puzzle_input, target_date))

    def test_puzzle1(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 543903
        self.assertEqual(puzzle_answer, PuzzleDay06.solve_puzzle_1(puzzle_input, "a"))

    # @parameterized.expand([
    #     ("turn on 0,0 through 0,0", 1),
    #     ("toggle 0,0 through 999,999", 2000000)
    # ])
    # def test_puzzle2_examples(self, puzzle_input, puzzle_solution):
    #     self.assertEqual(puzzle_solution, PuzzleDay06.solve_puzzle_2(puzzle_input))
    #
    # def test_puzzle2(self):
    #     puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
    #     puzzle_answer = 14687245
    #     self.assertEqual(puzzle_answer, PuzzleDay06.solve_puzzle_2(puzzle_input))


if __name__ == '__main__':
    unittest.main()
