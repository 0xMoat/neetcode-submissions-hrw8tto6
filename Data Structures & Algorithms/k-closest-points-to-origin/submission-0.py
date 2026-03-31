class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x,y in points:
            min_heap.append([math.sqrt(x**2+y**2), x, y])
        heapq.heapify(min_heap)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        return res

        # points.sort(key=lambda p: p[0]**2+p[1]**2)
        # return points[:k]