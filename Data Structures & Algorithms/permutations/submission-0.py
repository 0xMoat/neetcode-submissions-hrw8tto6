class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permute = []

        # i is upper layer index
        def dfs(i, visited_idx):
            if i >= len(nums):
                res.append(permute.copy())
                return

            for j in range(len(nums)):
                if j in visited_idx:
                    continue
                permute.append(nums[j])
                visited_idx.add(j)
                dfs(i+1, visited_idx)

                # backtracking
                permute.pop()
                visited_idx.remove(j)
        dfs(0, set())
        return res
            
                
