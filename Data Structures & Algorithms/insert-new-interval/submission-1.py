class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (start, end) in enumerate(intervals):
            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        res.append(newInterval)
        return res
        