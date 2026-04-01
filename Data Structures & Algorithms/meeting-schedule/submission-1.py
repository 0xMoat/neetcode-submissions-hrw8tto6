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
        last = None
        for interval in intervals:
            if not last or interval.start >= last.end:
                last = interval
            else:
                return False
                # last = [last[0], max(last[1], interval[1])]
        return True