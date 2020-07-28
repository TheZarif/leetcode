"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
# Complexity O(n)
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_dict={}
        def getNode(node):
            if node is None:
                return None
            if node not in node_dict:
                node_dict[node]=Node(node.val)
            return node_dict[node]

        node=head
        prev=None
        while node is not None:
            n=getNode(node)
            n.random=getNode(node.random)
            if prev:
                prev.next=n
            prev=n
            node=node.next
        return getNode(head)
