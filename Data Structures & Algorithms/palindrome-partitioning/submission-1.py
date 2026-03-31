class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []  # 存储当前切割出的回文串序列

        def dfs(i):
            # 基准情况：如果指针 i 走到了末尾，说明找到了一组完整的分割方案
            if i >= len(s):
                res.append(path[:]) # 注意要加 [:] 拷贝一份，否则 path 变化会影响结果
                return
            
            # 尝试从 i 开始的所有切割位置 j
            for j in range(i, len(s)):
                # 只有当 s[i:j+1] 是回文时，才继续往下切
                if self.isPali(s, i, j):
                    path.append(s[i:j+1]) # 1. 做选择
                    dfs(j + 1)            # 2. 递归处理剩余部分
                    path.pop()            # 3. 撤销选择（回溯）

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True