from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # edge case : single node list
        if not head.next:
            return None

        # find the length of the list
        length = 1
        p = head
        while p.next:
            length += 1
            p = p.next

        # edge case : first node is being removed
        if length-n == 0:
            head = head.next
            return head
        
        # find the node before the one being removed
        count = 1
        p2 = head
        while count != length-n:
            count += 1
            p2 = p2.next
        
        # remove the desired node
        next_node = p2.next.next
        p2.next = next_node
        
        return head
        
        