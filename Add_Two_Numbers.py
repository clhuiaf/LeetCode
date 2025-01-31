from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length_l1, length_l2 = 0, 0
        leading, secondary = None, None
        # find the length of l1 
        p = l1
        while p:
            length_l1 += 1
            p = p.next
        # find the length of l2   
        p = l2
        while p:
            length_l2 += 1
            p = p.next

        # determine leading list
        if length_l1 >= length_l2:
            leading = l1
            secondary = l2
        else:
            leading = l2
            secondary = l1

        # add two numbers 
        carry = 0
        new_head, tail = leading, leading
        while secondary and leading:
            total = leading.val + secondary.val + carry
            leading.val = total % 10
            if total >= 10:
                carry = 1
            else:
                carry = 0
            leading = leading.next
            secondary = secondary.next
            if tail.next:
                tail = tail.next 
        
        # edge case: two list has different length
        while leading:
            total = leading.val + carry 
            leading.val = total % 10
            if total >= 10:
                carry = 1
            else:
                carry = 0
            leading = leading.next
            if tail.next:
                tail = tail.next 
        
        # edge case: dealing with the remaining carry
        if carry > 0:
            tail.next = ListNode(carry)
        
        return new_head


