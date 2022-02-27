from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pass

    def reverse(self, s: List[str], start: int, end: int):
        if start >= end:
            return

        self.reverse(s, start + 1, end - 1)
        s[start], s[end] = s[end], s[start]
