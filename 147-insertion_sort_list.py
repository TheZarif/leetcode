# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Complexity Time O(n^2), Space O(1)
    def insertionSortList(self, head: ListNode) -> ListNode:
        node=head
        last=None
        
        while node is not None:
            nxt=node.next
            start=head
            prev=None
            if last:
                if last.val>node.val:
                    while start is not node:
                        if start.val>node.val:
                            if prev:
                                prev.next=node
                            else:
                                head=node
                            node.next=start
                            last.next=nxt
                            break
                        prev=start
                        start=start.next
                else:
                    last=node
            else:
                last=node
            node=nxt
        return head
