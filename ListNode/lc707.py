# design linked list
class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummyNode = LinkNode()

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        current = self.dummyNode.next
        while index > 0:
            current = current.next
            index = index - 1
        return current.val

    def addAtHead(self, val: int) -> None:
        tempNode = LinkNode(val)
        tempNode.next = self.dummyNode.next
        self.dummyNode.next = tempNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummyNode
        while current.next is not None:
            current = current.next
        current.next = LinkNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        else:
            current = self.dummyNode
            while index > 0:
                current = current.next
                index -= 1
            tempNode = LinkNode(val)
            tempNode.next = current.next
            current.next = tempNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index <= self.size - 1:
            current = self.dummyNode
            while index > 0:
                current = current.next
                index = index - 1
            current.next = current.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
