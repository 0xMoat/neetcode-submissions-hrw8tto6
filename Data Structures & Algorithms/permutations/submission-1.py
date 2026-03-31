class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()
        # i is upper layer index
        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue

                # choose branch
                path.append(nums[i])
                used.add(i)

                dfs()

                # backtracking
                path.pop()
                used.remove(i)

        dfs()
        return res
            
                
