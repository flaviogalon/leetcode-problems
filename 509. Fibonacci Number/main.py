from momoized_recursive import Solution as MemoizedSolution
from recursive import Solution

tests = [2, 3, 4, 7]
expected_results = [1, 2, 3, 13]

solution = Solution()
memoized_solution = MemoizedSolution()

for idx, test in enumerate(tests):
    result = solution.fib(test)
    assert result == expected_results[idx]

    result = memoized_solution.fib(test)
    assert result == expected_results[idx]
