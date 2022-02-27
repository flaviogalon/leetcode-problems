from loop import Solution as LoopSolution
from recursive import Solution as RecursiveSolution

tests = [["h", "e", "l", "l", "o"], ["H", "a", "n", "n", "a", "h"]]

expected_results = [["o", "l", "l", "e", "h"], ["h", "a", "n", "n", "a", "H"]]

for idx, test in enumerate(tests):
    loop_solution = LoopSolution()
    loop_solution.reverseString(test)
    assert test == expected_results[idx]

    recursive_solution = RecursiveSolution()
    recursive_solution.reverseString(test)
    assert test == expected_results[idx]
