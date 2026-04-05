# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        cur = head
        while cur:
            heapq.heappush(heap, cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            cur.val = heapq.heappop(heap)
            cur = cur.next

        return head
