class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(i, cur):
            if cur == target:
                res.append(path[:])

            for j in range(i, len(candidates)):
                if candidates[j] + cur > target:
                    break

                if j > i and candidates[j] == candidates[j-1]:
                    continue

                path.append(candidates[j])
                dfs(j+1, cur + candidates[j])
                path.pop()

        dfs(0,0)
        return res
