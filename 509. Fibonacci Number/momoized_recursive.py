class Solution:

    memo = {}

    def fib(self, n: int) -> int:
        return self._fib(n)

    def _fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        if n - 1 not in self.memo:
            self.memo[n - 1] = self._fib(n - 1)
        if n - 2 not in self.memo:
            self.memo[n - 2] = self._fib(n - 2)

        return self.memo[n - 1] + self.memo[n - 2]
