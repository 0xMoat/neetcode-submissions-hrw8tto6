class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset):
            # 每一个状态都是结果：
            # 在子集问题中，递归树的每一个节点（包括根节点空集 []）
            # 都是一个有效的子集
            res.append(subset[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])
                dfs(j+1, subset)
                subset.pop()
                # dfs(j+1, subset)

        dfs(0,[])
        return res