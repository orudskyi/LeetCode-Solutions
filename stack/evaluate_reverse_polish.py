"""
150. Evaluate Reverse Polish Notation
Category: Stack
Link: https://neetcode.io/problems/evaluate-reverse-polish-notation/question?list=neetcode150
Difficulty: Medium
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))

        return stack[0]


def test_plus_one():
    s = Solution()
    assert s.evalRPN(["1", "2", "+", "3", "*", "4", "-"]) == 5
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22


if __name__ == "__main__":
    solver = Solution()

    result = solver.evalRPN(["1", "2", "+", "3", "*", "4", "-"])

    print(f"Result:    {result}")
