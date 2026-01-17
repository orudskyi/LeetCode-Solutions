"""
20. Valid Parentheses
Category: Stack
Link: https://leetcode.com/problems/valid-parentheses/description/
Difficulty: Easy
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


def test_plus_one():
    s = Solution()
    assert s.isValid("([{}])")
    assert not s.isValid("[(])")


if __name__ == "__main__":
    solver = Solution()

    result = solver.isValid("[()]")

    print(f"Result:    {result}")
