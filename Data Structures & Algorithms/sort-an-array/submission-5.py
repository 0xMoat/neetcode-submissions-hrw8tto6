import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quick sort
        return self.quickSort(nums, 0, len(nums) -1)

    def quickSort(self, arr, lo, hi):
        if lo >= hi:
            return arr
        p = self.partition(arr, lo, hi)
        self.quickSort(arr, lo, p-1)
        self.quickSort(arr, p+1, hi)
        return arr

    def partition(self, arr, lo, hi):
        # 随机选pivot，交换到末尾
        rand_idx = random.randint(lo, hi)
        arr[rand_idx], arr[hi] = arr[hi], arr[rand_idx]

        pivot = arr[hi]
        i = lo - 1
        for j in range(lo,hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[hi] = arr[hi], arr[i+1]
        return i+1