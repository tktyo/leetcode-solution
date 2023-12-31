# Linked list cycle
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define slow pointer and fast pointer
        slow = head
        fast = head
        temp = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while temp is not slow:
                    temp = temp.next
                    slow = slow.next
                return temp

        return None
