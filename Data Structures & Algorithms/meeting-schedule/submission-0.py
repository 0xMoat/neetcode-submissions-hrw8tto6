"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))
        temp = None
        for interval in intervals:
            if not temp or interval.start >= temp.end:
                temp = interval
            else:
                return False
        return True