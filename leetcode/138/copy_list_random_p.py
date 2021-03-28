"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Modify original structure: Original->Copy->Original->Copy
        # node.next.random = node.random.next
        # O(n) and O(1)
        p = head
        while p is not None:
            next = p.next
            copy = Node(p.val)
            p.next = copy
            copy.next =  next
            p = next
        p = head
        while p is not None:
            if p.random is not None:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        if p is not None:
            headCopy = p.next
        else:
            headCopy = None
        while p is not None:
            copy = p.next
            p.next = copy.next
            p = p.next
            if p is not None:
                copy.next = p.next
        return headCopy
