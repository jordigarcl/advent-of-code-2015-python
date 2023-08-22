import os
import re
import unittest

from parameterized import parameterized


class PuzzleDay06:

    @staticmethod
    def solve_puzzle_1(puzzle_input, target_gate):
        mask16 = 0xFFFF

        class Gate:
            def __init__(self, gate_type, name, input_gates, input_param=None):
                self.gate_type = gate_type
                self.name = name
                self.input_gates = input_gates
                self.input_param = int(input_param) & mask16 if input_param is not None else None

            def resolve_output_value(self, circuit):

                if self.gate_type == "NOT":
                    val = circuit.get_gate(self.input_gates[0]).resolve_output_value(circuit)
                    return (~val) & mask16
                elif self.gate_type == "AND":
                    val1 = circuit.get_gate(self.input_gates[0]).resolve_output_value(circuit)
                    val2 = circuit.get_gate(self.input_gates[1]).resolve_output_value(circuit)
                    return (val1 & val2) & mask16
                elif self.gate_type == "OR":
                    val1 = circuit.get_gate(self.input_gates[0]).resolve_output_value(circuit)
                    val2 = circuit.get_gate(self.input_gates[1]).resolve_output_value(circuit)
                    return (val1 | val2) & mask16
                elif self.gate_type == "LSHIFT":
                    val1 = circuit.get_gate(self.input_gates[0]).resolve_output_value(circuit)
                    val2 = self.input_param
                    return (val1 << val2) & mask16
                elif self.gate_type == "RSHIFT":
                    val1 = circuit.get_gate(self.input_gates[0]).resolve_output_value(circuit)
                    val2 = self.input_param
                    return (val1 >> val2) & mask16
                elif self.gate_type == "DIRECT_VALUE":
                    val = self.input_param
                    return (val) & mask16
                elif self.gate_type == "DIRECT_GATE":
                    val = circuit.get_gate(self.input_gates[0]).resolve_output_value(circuit)
                    return (val) & mask16
                else:
                    raise Exception("this should not happen")

        class Circuit:
            def __init__(self):
                self.gates = dict()

            def get_gate(self, gate_name):
                print(gate_name)
                return self.gates[gate_name]

            def add_gate_not(self, input_wire_name, output_wire_name):
                self.gates[output_wire_name] = Gate("NOT", output_wire_name, [input_wire_name])

            def add_gate_and(self, input_1_wire_name, input_2_wire_name, output_wire_name):
                self.gates[output_wire_name] = Gate("AND", output_wire_name, [input_1_wire_name, input_2_wire_name])

            def add_gate_or(self, input_1_wire_name, input_2_wire_name, output_wire_name):
                self.gates[output_wire_name] = Gate("OR", output_wire_name, [input_1_wire_name, input_2_wire_name])

            def add_gate_lshift(self, input_wire_name, input_param, output_wire_name):
                self.gates[output_wire_name] = Gate("LSHIFT", output_wire_name, [input_wire_name], input_param)

            def add_gate_rshift(self, input_wire_name, input_param, output_wire_name):
                self.gates[output_wire_name] = Gate("RSHIFT", output_wire_name, [input_wire_name], input_param)

            def add_gate_direct_value(self, input_param, output_wire_name):
                self.gates[output_wire_name] = Gate("DIRECT_VALUE", output_wire_name, [], input_param)

            def add_gate_direct_gate(self, input_wire_name, output_wire_name):
                self.gates[output_wire_name] = Gate("DIRECT_GATE", output_wire_name, [input_wire_name])

        def build_circuit(puzzle_input):

            regex_not = r'NOT (\w+) -> (\w+)'
            regex_and = r'(\w+) AND (\w+) -> (\w+)'
            regex_or = r'(\w+) OR (\w+) -> (\w+)'
            regex_lshift = r'(\w+) LSHIFT (\d+) -> (\w+)'
            regex_rshift = r'(\w+) RSHIFT (\d+) -> (\w+)'
            regex_direct_val = r'(\d+) -> (\w+)'
            regex_direct_gate = r'(\w+) -> (\w+)'

            circuit = Circuit()

            for line in puzzle_input.splitlines():
                if "NOT" in line:
                    # e.g. "NOT x -> h"
                    match = re.match(regex_not, line)
                    input_wire_name = match.group(1)  # e.g. "x"
                    output_wire_name = match.group(2)  # e.g. "h"
                    circuit.add_gate_not(input_wire_name, output_wire_name)
                elif "AND" in line:
                    # e.g. "x AND y -> d"
                    match = re.match(regex_and, line)
                    input_1_wire_name = match.group(1)  # e.g. "x"
                    input_2_wire_name = match.group(2)  # e.g. "y"
                    output_wire_name = match.group(3)  # e.g. "d"
                    circuit.add_gate_and(input_1_wire_name, input_2_wire_name, output_wire_name)
                elif "OR" in line:
                    # e.g. "x OR y -> e"
                    match = re.match(regex_or, line)
                    input_1_wire_name = match.group(1)  # e.g. "x"
                    input_2_wire_name = match.group(2)  # e.g. "y"
                    output_wire_name = match.group(3)  # e.g. "e"
                    circuit.add_gate_or(input_1_wire_name, input_2_wire_name, output_wire_name)
                elif "LSHIFT" in line:
                    # e.g. "x LSHIFT 2 -> f"
                    match = re.match(regex_lshift, line)
                    print(line, match)
                    input_wire_name = match.group(1)  # e.g. "x"
                    input_param = match.group(2)  # e.g. "2" TODO byte?
                    output_wire_name = match.group(3)  # e.g. "f"
                    circuit.add_gate_lshift(input_wire_name, input_param, output_wire_name)
                elif "RSHIFT" in line:
                    # e.g. "y RSHIFT 2 -> g"
                    match = re.match(regex_rshift, line)
                    input_wire_name = match.group(1)  # e.g. "y"
                    input_param = match.group(2)  # e.g. "2" TODO byte?
                    output_wire_name = match.group(3)  # e.g. "g"
                    circuit.add_gate_rshift(input_wire_name, input_param, output_wire_name)
                else:
                    # e.g. "123 -> x"
                    match = re.match(regex_direct_val, line)
                    if match is not None:
                        input_param = match.group(1)  # e.g. "2" TODO byte?
                        output_wire_name = match.group(2)  # e.g. "y"
                        circuit.add_gate_direct_value(input_param, output_wire_name)
                    else:
                        # e.g. "lx -> a"
                        match = re.match(regex_direct_gate, line)
                        input_wire_name = match.group(1)  # e.g. "lx"
                        output_wire_name = match.group(2)  # e.g. "a"
                        circuit.add_gate_direct_gate(input_wire_name, output_wire_name)

            return circuit

        circuit = build_circuit(puzzle_input)

        return circuit.get_gate(target_gate).resolve_output_value(circuit)

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
