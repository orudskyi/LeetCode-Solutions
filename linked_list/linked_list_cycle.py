"""
Problem 141. Linked List Cycle
Category: Linked List
Link: https://neetcode.io/problems/linked-list-cycle-detection/question
Difficulty: Easy
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def list_to_linkedlist(elements: list[int]) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    for val in elements:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(head: ListNode) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    elements = [1, 2, 3, 4]
    head = list_to_linkedlist(elements)

    current = head
    tail = None
    node_to_connect_to = None
    index = 0
    pos = 1 

    while current.next:
        if index == pos:
            node_to_connect_to = current
        current = current.next
        index += 1
    
    tail = current 
    
    if node_to_connect_to is None and index == pos: 
         node_to_connect_to = tail

    if tail and node_to_connect_to:
        tail.next = node_to_connect_to
        print(f"Cycle created: Tail ({tail.val}) connects to Node ({node_to_connect_to.val})")
    
    solution = Solution()
    print(f"Test 2 (With Cycle): {solution.hasCycle(head)}") # Має бути True
