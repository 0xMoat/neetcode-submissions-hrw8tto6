"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originToCopy = {None: None}
        curr = head
        while curr:
            originToCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = originToCopy[curr]
            copy.next = originToCopy[curr.next]
            copy.random = originToCopy[curr.random]
            curr = curr.next

        return originToCopy[head]