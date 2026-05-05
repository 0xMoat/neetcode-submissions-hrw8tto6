class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []  # 存 index
        res2 = [0]*len(nums)

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
                res2[idx] = i-idx
            stack.append(i)
            print(stack)

        return res2