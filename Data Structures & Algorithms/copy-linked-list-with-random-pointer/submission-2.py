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
        origin_to_copy = {None:None}
        curr = head
        while curr:
            origin_to_copy[curr] = Node(curr.val)
            curr = curr.next

        for origin, copy in origin_to_copy.items():
            if not origin:
                continue
            copy.next = origin_to_copy[origin.next]
            copy.random = origin_to_copy[origin.random]

        return origin_to_copy[head]