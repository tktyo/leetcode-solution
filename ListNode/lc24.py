# swap Nodes in Pairs
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        current = dummyHead
        while current.next is not None and current.next.next is not None:
            temp1 = current.next
            temp2 = temp1.next

            current.next = temp2
            temp1.next = temp2.next
            temp2.next = temp1

            current = temp1
        return dummyHead.next
