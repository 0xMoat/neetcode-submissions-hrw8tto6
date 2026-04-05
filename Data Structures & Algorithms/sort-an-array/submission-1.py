class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort
        n = len(nums)
        sortedIndex = 0
        while sortedIndex < n:
            for i in range(n-1, sortedIndex - 1, -1):
                if nums[i] < nums[i-1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            
            sortedIndex += 1
        return nums