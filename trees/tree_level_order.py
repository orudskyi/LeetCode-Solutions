"""
Problem 102. Binary Tree Level Order Traversal
Category: Trees
Link: https://neetcode.io/problems/level-order-traversal-of-binary-tree/question
Difficulty: Medium
"""

import collections
from typing import Optional
from tree_utils import TreeNode, list_to_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            queue_len = len(queue)

            for _ in range(queue_len):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)

        return result


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7]
    print(f"Input List:  {input_list}")

    root = list_to_tree(input_list)
    sol = Solution()

    res = sol.levelOrder(root)

    print(f"Result is {res}")

    expected = [[1], [2, 3], [4, 5, 6, 7]]

    assert res == expected, "Test Failed"
    print("✅ Test successful!")
