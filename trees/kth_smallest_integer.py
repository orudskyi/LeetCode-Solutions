"""
Problem 230. Kth Smallest Element in a BST
Category: Trees
Link: https://neetcode.io/problems/kth-smallest-integer-in-bst/question
Difficulty: Medium
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]


if __name__ == "__main__":
    input_list = [5, 3, 6, 2, 4, None, None, 1]
    print(f"Input List:  {input_list}")

    root = list_to_tree(input_list)
    sol = Solution()

    res = sol.kthSmallest(root, 3)

    print(f"Result is {res}")

    expected = 3

    assert res == expected, "Test Failed"
    print("✅ Test successful!")
