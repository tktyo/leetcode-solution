# remove linked list elements
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tempHead = ListNode()
        tempHead.next = head

        previous = tempHead
        p = head

        while p is not None:
            if p.val == val:
                previous.next = p.next
                p = previous.next
            else:
                previous = p
                p = p.next

        return tempHead.next
