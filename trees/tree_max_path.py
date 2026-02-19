"""
Problem 124. Binary Tree Maximum Path Sum
Category: Trees
Link: https://neetcode.io/problems/binary-tree-maximum-path-sum/question
Difficulty: Hard
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
        
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            current_sum = node.val + left_max + right_max
            res[0] = max(res[0], current_sum)
            
            return node.val + max(left_max, right_max)
        
        dfs(root)
        
        return res[0]


if __name__ == "__main__":
    input_list = [-10, 9, 20, None, None, 15, 7]
    print(f"Input List:  {input_list}")

    root = list_to_tree(input_list)
    sol = Solution()

    res = sol.maxPathSum(root)

    print(f"Result is {res}")

    expected = 42

    assert res == expected, "Test Failed"
    print("✅ Test successful!")
