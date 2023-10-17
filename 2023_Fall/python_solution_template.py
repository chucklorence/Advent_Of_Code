# This is the template for solutions written in Python!

# Start by copying this template and saving it as, for example, `day1solution.py`.
# Then, change the file location in the line `Day1Solver("template-input.txt")`,
# so that it points to the file with your input.
# After that, fillin (or change!) the code (and documentation!) to solve the problem.
# Finally, run your code (and obtain the answers) by typing `python day1solution.py`
# into a terminal.


class Day1Solver():
    def __init__(self, file_path: str):
        """Load and parse puzzle input"""
        with open(file_path) as f:
            self.raw_input = [x.strip() for x in f.readlines()]
        # TODO: If necessary, change the code below to include any
        # other manipulations you'd like to make to the raw input
        self.input = [int(x) for x in self.raw_input]

    def solve_part1(self) -> int:
        """TODO: Write a documentation string for your solution to Part 1"""
        # TODO: Replace the code below with your code to solve Part 1.
        return sum(self.input)

    def solve_part2(self) -> int:
        """"TODO: Write a documentation string for your solution to Part 2"""
        # TODO: Replace the code below with your code to solve Part 2.
        return sum([x**2 for x in self.input])


if __name__ == "__main__":
    solver = Day1Solver("template-input.txt")
    print('The solution to part 1 is', solver.solve_part1())
    print('The solution to part 2 is', solver.solve_part2())