"""
Problem 235. Lowest Common Ancestor of a Binary Search Tree
Category: Trees
Link: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree/question?list=blind75
Difficulty: Medium
"""

from typing import Optional
from tree_utils import TreeNode, list_to_tree

class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        return None

# --- Helper function for testing ---
def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Finds a node with a specific value in a BST."""
    curr = root
    while curr:
        if val == curr.val:
            return curr
        elif val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None

if __name__ == "__main__":
    # 1. Create the main tree
    input_list = [5, 3, 8, 1, 4, 7, 9, None, 2]
    print(f"Input List:  {input_list}")
    root = list_to_tree(input_list)
    
    # 2. Find the ACTUAL nodes p and q inside the tree
    p_node = search_bst(root, 3)
    q_node = search_bst(root, 8)
    
    assert p_node is not None, "Node p not found in tree"
    assert q_node is not None, "Node q not found in tree"

    # 3. Run solution
    sol = Solution()
    res_node = sol.lowestCommonAncestor(root, p_node, q_node)

    if res_node:
        print(f"Result Node Value: {res_node.val}")
    else:
        print("Result is None")

    expected_val = 5

    # 4. Check the result
    assert res_node is not None and res_node.val == expected_val, "Test Failed"
    print("✅ Test successful!")