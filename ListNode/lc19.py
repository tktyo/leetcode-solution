# remove Nth Node from End of List
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead = ListNode()
        tempHead.next = head
        temp1 = tempHead
        temp2 = tempHead
        while temp2.next is not None:
            if n != 0:
                temp2 = temp2.next
                n = n - 1
            else:
                temp1 = temp1.next
                temp2 = temp2.next
        temp1.next = temp1.next.next
        return tempHead.next
