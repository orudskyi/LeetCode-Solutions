"""
Problem 105. Construct Binary Tree from Preorder and Inorder Traversal
Category: Trees
Link: https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal/question
Difficulty: Medium
"""

from typing import List
from typing import Optional
from tree_utils import TreeNode, list_to_tree, tree_to_list


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root


if __name__ == "__main__":
    preorder_list = [1, 2, 3, 4]
    inorder_list = [2, 1, 3, 4]
    print(f"Input preorder:  {preorder_list}")
    print(f"Input inorder:  {inorder_list}")

    sol = Solution()

    res_tree = sol.buildTree(preorder_list, inorder_list)
    res_list = tree_to_list(res_tree)

    print(f"Result is {res_list}")

    expected = [1, 2, 3, None, None, None, 4]

    assert res_list == expected, "Test Failed"
    print("✅ Test successful!")
