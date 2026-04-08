import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # another quick sort
        if len(nums) <= 1:
            return nums

        idx = random.randint(0, len(nums)-1)
        pivot = nums[idx]
        left = [n for n in nums if n < pivot]
        middle = [n for n in nums if n == pivot]
        right = [n for n in nums if n > pivot]

        return self.sortArray(left) + middle + self.sortArray(right)