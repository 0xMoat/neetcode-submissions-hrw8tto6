class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []

        def dfs(i, total):
            if total == target:
                res.append(combination.copy())
                return

            if i >= len(candidates) or total > target:
                return

            combination.append(candidates[i])
            dfs(i+1, total+candidates[i])
            combination.pop()
            # # 跳过所有与 candidates[i] 相同的元素，再递归
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res
