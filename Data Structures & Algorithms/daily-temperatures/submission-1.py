class Solution:
    def dailyTemperatures(self, tmperatures: List[int]) -> List[int]:
        res=[0] * len(tmperatures)
        stack = []# stack save the idx of days haven't found higher temperature

        for i in range(len(tmperatures)):
            while stack and tmperatures[i] > tmperatures[stack[-1]]:
                idx_to_calculate = stack.pop()
                res[idx_to_calculate] = i - idx_to_calculate
            stack.append(i)
        
        return res