"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = [inter.start for inter in intervals]
        end = [inter.end for inter in intervals]
        start.sort()
        end.sort()
        
        i, j = 0, 0
        res, count = 0, 0
        while i < n and j < n:
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)

        return res

