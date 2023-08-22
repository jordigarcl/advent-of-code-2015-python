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

    @staticmethod
    def solve_puzzle_2(puzzle_input, target_gate):
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

            def add_gate(self, gate):
                self.gates[gate.name] = gate

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
        # Now, take the signal you got on wire a, override wire b to that signal...
        circuit.add_gate(Gate("DIRECT", "b", ["46065"]))

        return circuit.get_gate(target_gate).resolve_output()


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
        puzzle_answer = 46065
        self.assertEqual(puzzle_answer, PuzzleDay06.solve_puzzle_1(puzzle_input, "a"))

    def test_puzzle2(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 14687245
        self.assertEqual(puzzle_answer, PuzzleDay06.solve_puzzle_2(puzzle_input, "a"))


if __name__ == '__main__':
    unittest.main()
