class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dic = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            course_dic[c].append(p)

        visited = set()

        def dfs(c):
            if c in visited:
                return False

            if course_dic[c] == []:
                return True

            visited.add(c)
            for p in course_dic[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            course_dic[c] = []
            return True

        for c in course_dic:
            if not dfs(c):
                return False

        return True