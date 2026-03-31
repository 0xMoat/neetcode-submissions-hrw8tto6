class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        res = [intervals[0]]
        for idx in range(1, len(intervals)):
            lb, le = res[-1]
            nb, ne = intervals[idx]
            if nb <= le:
                res[-1][1] = max(le, ne)
                print("!", res[-1])
            else:
                res.append(intervals[idx])
            print(lb, le, nb, ne, res)
        return res