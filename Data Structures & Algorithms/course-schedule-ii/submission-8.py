class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_dic = {n:[] for n in range(numCourses)}
        for c, p in prerequisites:
            course_dic[c].append(p)

        visiting = set()
        completed = set()
        res = []
        print()
        def dfs(c):
            if c in visiting:
                return False

            if c in completed:
                print(visiting, c, completed)
                return True

            visiting.add(c)
            for p in course_dic[c]:
                if not dfs(p):
                    return False

            visiting.remove(c)
            # 表示 c 所依赖的所有先修课（Prerequisites）都已经先于它处理完毕
            completed.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
