class Solution:
    def fib(self, n: int) -> int:
        return self._fib(n)

    def _fib(self, n:int) -> int:
        if n == 0 or n == 1:
            return n
        return self._fib(n - 1) + self._fib(n - 2)