    
class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
        
    def __repr__(self):
        return '<' + str(self.val) + ', next: ' + str(self.next) + '>'
        
class MyLinkedList:

            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.len=0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node=self.head
        idx=0
        while node is not None:
            if idx==index:
                return node.val
            idx+=1
            node=node.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        n=Node(val)
        if self.head:
            n.next=self.head
        self.head=n
        self.len+=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        n=Node(val)
        node=self.head
        prev=None
        while node is not None:
            prev=node
            node=node.next
        if prev:
            prev.next=n
        else:
            self.head=n
        self.len+=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index>=0 and index<=self.len:
            n=Node(val)
            node=self.head
            prev=None
            idx=0
            while node is not None:
                if idx==index:
                    n.next=node
                    if prev:
                        prev.next=n
                    else:
                        self.head=n
                    self.len+=1
                    return
                idx+=1
                prev=node
                node=node.next
            if prev:
                prev.next=n
            else:
                self.head=n
            self.len+=1
            return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index>=0 and index<self.len:
            node=self.head
            prev=None
            idx=0
            while node is not None:
                if idx==index:
                    if prev:
                        prev.next=node.next
                    else:
                        self.head=node.next
                    del node
                    self.len-=1

                    return
                idx+=1
                prev=node
                node=node.next
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
