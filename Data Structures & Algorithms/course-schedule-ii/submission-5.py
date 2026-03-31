class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_dic = {n:[] for n in range(numCourses)}
        for c, p in prerequisites:
            course_dic[c].append(p)

        visited = set()
        completed = set()
        res = []

        def dfs(c):
            if c in visited:
                return False

            if c in completed:
                return True

            visited.add(c)
            for p in course_dic[c]:
                if not dfs(p):
                    return False

            visited.remove(c)
            # 表示 c 所依赖的所有先修课（Prerequisites）都已经先于它处理完毕
            completed.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
