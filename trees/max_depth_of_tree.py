"""
Problem 104. Maximum Depth of Binary Tree
Category: Trees
Link: https://neetcode.io/problems/depth-of-binary-tree/question?list=blind75
Difficulty: Easy
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    input_list = [1, 2, 3, None, None, 4]
    print(f"Input List:  {input_list}")

    root = list_to_tree(input_list)
    sol = Solution()

    res = sol.maxDepth(root)

    print(f"Result is {res}")

    expected = 3

    assert res == expected, "Test Failed"
    print("✅ Test successful!")
