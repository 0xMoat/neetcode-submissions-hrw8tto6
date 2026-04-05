class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sortedIndex = 0
        while sortedIndex < n:
            minIndex = sortedIndex
            for i in range(sortedIndex+1, n):
                if nums[minIndex] > nums[i]:
                    minIndex = i
            nums[minIndex], nums[sortedIndex] = nums[sortedIndex], nums[minIndex]
            sortedIndex += 1
        return nums