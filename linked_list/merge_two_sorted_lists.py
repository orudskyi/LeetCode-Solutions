"""
Problem 21. Merge Two Sorted Lists
Category: Linked List
Link: https://neetcode.io/problems/merge-two-sorted-linked-lists/question
Difficulty: Easy
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next


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
    list1 = [1, 2, 4]
    list2 = [1, 3, 5]
    head1 = list_to_linkedlist(list1)
    head2 = list_to_linkedlist(list2)

    solution = Solution()
    new_head = solution.mergeTwoLists(head1, head2)

    print(f"Output: {linkedlist_to_list(new_head)}")
