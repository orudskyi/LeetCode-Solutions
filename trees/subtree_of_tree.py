"""
Problem 572. Subtree of Another Tree
Category: Trees
Link: https://neetcode.io/problems/subtree-of-a-binary-tree/question
Difficulty: Easy
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))
        else:
            return False


if __name__ == "__main__":
    input_list_1 = [1,2,3,4,5,None,None,6]
    input_list_2 = [2, 4, 5]
    print(f"Input List:  {input_list_1}")
    print(f"Input List:  {input_list_2}")

    root_1 = list_to_tree(input_list_1)
    root_2 = list_to_tree(input_list_2)

    sol = Solution()
    result = sol.isSubtree(root_1, root_2)

    # output_list = tree_to_list(inverted_root)

    print(f"Result: {result}")

    expected = False
    assert result == expected, "Test Failed!"
    print("✅ Test successful!")
