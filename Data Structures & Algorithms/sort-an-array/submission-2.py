class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort
        n = len(nums)
        sortedIndex = 0
        while sortedIndex < n:
            swapped = False
            for i in range(n-1, sortedIndex - 1, -1):
                if nums[i] < nums[i-1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    swapped = True
            
            if not swapped:
                break
            sortedIndex += 1
        return nums