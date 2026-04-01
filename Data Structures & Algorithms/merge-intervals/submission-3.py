class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: (pair[0], pair[1]))
        res = []

        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res
            