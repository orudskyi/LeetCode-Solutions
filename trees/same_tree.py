"""
Problem 100. Same Tree
Category: Trees
Link: https://neetcode.io/problems/same-binary-tree/question?list=blind75
Difficulty: Easy
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


if __name__ == "__main__":
    input_list_1 = [4, 7, 9]
    input_list_2 = [4, 7, 9]
    print(f"Input List:  {input_list_1}")
    print(f"Input List:  {input_list_2}")

    root_1 = list_to_tree(input_list_1)
    root_2 = list_to_tree(input_list_2)

    sol = Solution()
    result = sol.isSameTree(root_1, root_2)

    # output_list = tree_to_list(inverted_root)

    print(f"Result: {result}")

    expected = True
    assert result == expected, "Test Failed!"
    print("✅ Test successful!")
