from stack import Solution as StackSolution

problems = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
expected_answers = ["aaabcbc", "accaccacc", "abcabccdcdcdef"]

stack = StackSolution()

for idx, problem in enumerate(problems):
    solution = stack.decodeString(problem)
    assert solution == expected_answers[idx]