class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return len(intervals) - self.intervalSchedual(intervals)

    # calculate max non-overlapping interval
    def intervalSchedual(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[1])
        xEnd = intervals[0][1]
        count = 1
        for interval in intervals:
            start = interval[0]
            if start >= xEnd:
                count += 1
                xEnd = interval[1]
        return count