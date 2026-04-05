# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        while cur:
            tmp = head
            while tmp != cur:
                if tmp.val > cur.val:
                    tmp.val, cur.val = cur.val, tmp.val
                tmp = tmp.next
            cur = cur.next
        return head



    def insertionSortListClassic(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            next_temp = curr.next
            prev.next, curr.next = curr, prev.next
            curr = next_temp
        return dummy.next

    def insertsort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            # 因为nums[j] <= key 的时候就停止移动
            # 所以相等的元素之前的顺序还在，所以这个排序算法是稳定的
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
            nums[j+1] = key
            
        return nums
        






