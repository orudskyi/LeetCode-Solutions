"""
Problem 206. Reverse Linked List
Category: Linked List
Link: https://neetcode.io/problems/reverse-a-linked-list/question
Difficulty: Easy
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    

def list_to_linkedlist(elements: list[int]) -> ListNode:
    """Перетворює [1, 2, 3] -> 1 -> 2 -> 3"""
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
    input_values = [1, 2, 3, 4, 5]
    head = list_to_linkedlist(input_values)
    
    print(f"Input:  {linkedlist_to_list(head)}")

    solution = Solution()
    new_head = solution.reverseList(head)

    print(f"Output: {linkedlist_to_list(new_head)}")