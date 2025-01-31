from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # We need at least three nodes for the reordering
        if not head or not head.next or not head.next.next:
            return None

        slow, fast = head, head
        # Split the linked-list into two parts
        while (fast and fast.next) and slow:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second part
        prev, curr = slow.next, slow.next.next
        slow.next = None # Set nullptr as the tail of first part
        prev.next = None # Set nullptr as the tail of the reversed second part
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Reorder the linked list
        first_head, second_head = head, prev
        while second_head:
            first_next_node = first_head.next
            second_next_node = second_head.next
            first_head.next = second_head
            second_head.next = first_next_node
            first_head = first_next_node
            second_head = second_next_node

        return None


        
            