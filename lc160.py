# Intersection of two linked lists
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lA = 0
        lB = 0
        tempHeadA = headA
        tempHeadB = headB
        while tempHeadA is not None:
            lA += 1
            tempHeadA = tempHeadA.next
        while tempHeadB is not None:
            lB += 1
            tempHeadB = tempHeadB.next

        tempHeadA = headA
        tempHeadB = headB
        while tempHeadA is not None and tempHeadB is not None:
            if lA > lB:
                tempHeadA = tempHeadA.next
                lA = lA - 1
            elif lA < lB:
                tempHeadB = tempHeadB.next
                lB = lB - 1
            else:
                if tempHeadA == tempHeadB:
                    return tempHeadA
                else:
                    tempHeadA = tempHeadA.next
                    tempHeadB = tempHeadB.next
        return None
