class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat

                repeat = int(repeat)
                stack.append(substring * repeat)

        return "".join(stack)
