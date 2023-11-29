import unittest
import os
import re


class PuzzleDay09:

    @staticmethod
    def solve_puzzle_1(puzzle_input):
        class World:
            def __init__(self, puzzle_input):
                self.cities = {}
                regex = r"(\w+) to (\w+) = (\d+)"
                for line in puzzle_input.splitlines():
                    # e.g. "Dublin to Belfast = 141"
                    match = re.match(regex, line)
                    city_1 = match.group(1)  # Dublin
                    city_2 = match.group(2)  # Belfast
                    distance = int(match.group(3))  # 141

                    if city_1 not in self.cities:
                        self.cities[city_1] = {}

                    self.cities[city_1][city_2] = distance

                    if city_2 not in self.cities:
                        self.cities[city_2] = {}
                    self.cities[city_2][city_1] = distance

            def get_cities(self):
                return self.cities.keys()

            def evaluate_shortest_tour_distance_from(self, city):
                return self.traverse([{city: 0}], None)

            def traverse(self, breadcrumbs, min_total_distance):
                current_city = breadcrumbs[-1]
                nonvisited_neighbouring_cities = [city for city in (self.cities[current_city]) if
                                                  city not in breadcrumbs]

                if len(nonvisited_neighbouring_cities) <= 0:  # No more cities to visit!
                    if len(breadcrumbs) != len(self.cities):  # A dead end!
                        return None
                    else:  # We visited all cities!
                        total_distance = sum([city.value for city in breadcrumbs])
                        return min(total_distance, min_total_distance) if min_total_distance is not None else total_distance

                for next_city in nonvisited_neighbouring_cities:
                    distance = current_city[next_city]
                    breadcrumbs.append({next_city: distance})
                    total_distance = self.traverse(breadcrumbs)
                    min(total_distance, min_total_distance) if min_total_distance is not None else total_distance

                breadcrumbs.pop()

        # == Main ==
        world = World(puzzle_input)
        return min([world.evaluate_shortest_tour_distance_from(city) for city in world.get_cities()])

    # @staticmethod
    # def solve_puzzle_2(puzzle_input):
    #
    #     def process_lines(lines):
    #         for line in lines:
    #             encoded_string = line.encode("unicode_escape").decode('utf-8').replace("\"", "\\\"")
    #             print(f'{line} -> {encoded_string}')
    #             yield (len(encoded_string) + 2) - len(line)
    #
    #     return sum(list(process_lines(puzzle_input.splitlines())))


class TestPuzzleDay06(unittest.TestCase):

    def test_puzzle1_examples(self):
        puzzle_input = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
        puzzle_solution = 605
        self.assertEqual(puzzle_solution, PuzzleDay09.solve_puzzle_1(puzzle_input))

    def test_puzzle1(self):
        puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
        puzzle_answer = 1350
        self.assertEqual(puzzle_answer, PuzzleDay09.solve_puzzle_1(puzzle_input))


#     def test_puzzle2_examples(self):
#         puzzle_input = """\"\"
# \"abc\"
# \"aaa\\\"aaa"
# \"\\x27\""""
#         puzzle_solution = 19
#         self.assertEqual(puzzle_solution, PuzzleDay09.solve_puzzle_2(puzzle_input))
#
#     def test_puzzle2(self):
#         puzzle_input = open(os.path.join(os.path.dirname(__file__), 'input_puzzle.txt'), "r").read()
#         puzzle_answer = 2085
#         self.assertEqual(puzzle_answer, PuzzleDay09.solve_puzzle_2(puzzle_input))
#

if __name__ == '__main__':
    unittest.main()
