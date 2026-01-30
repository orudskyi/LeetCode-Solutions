"""
Problem 226. Invert Binary Tree
Category: Trees
Link: https://neetcode.io/problems/invert-a-binary-tree/question
Difficulty: Easy
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree, tree_to_list

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

if __name__ == "__main__":
    input_list = [4, 2, 7, 1, 3, 6, 9]
    print(f"Input List:  {input_list}")

    root = list_to_tree(input_list)
    
    sol = Solution()
    inverted_root = sol.invertTree(root)
    
    output_list = tree_to_list(inverted_root)
    
    print(f"Output List: {output_list}")
    
    expected = [4, 7, 2, 9, 6, 3, 1]
    assert output_list == expected, "Test Failed!"
    print("✅ Test successful!")
    
    