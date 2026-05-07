class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m

            # if left part has ascending order
            # minimum num in right part
            if nums[l] <= nums[m]:
                # IMPORTANT! if target in left part
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else: # continue search in right part
                    l = m + 1

            # if right part has ascending order
            # minimum num in left part
            else:
                # IMPORTANT! if target in right part
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else: # continue search in left part
                    r = m - 1

        return -1