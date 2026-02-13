"""
Problem 98. Validate Binary Search Tree
Category: Trees
Link: https://neetcode.io/problems/valid-binary-search-tree/question
Difficulty: Medium
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right)) 
            
        return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    input_list = [5, 1, 4, None, None, 3, 6]
    print(f"Input List:  {input_list}")

    root = list_to_tree(input_list)
    sol = Solution()

    res = sol.isValidBST(root)

    print(f"Result is {res}")

    expected = False

    assert res == expected, "Test Failed"
    print("✅ Test successful!")
