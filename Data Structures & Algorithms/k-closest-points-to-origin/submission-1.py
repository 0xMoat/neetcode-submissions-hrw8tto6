class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [ ((x**2 + y**2), x, y) for (x, y) in points]
        heapq.heapify(pq)
        res = []

        for _ in range(k):
            dist, x, y = heapq.heappop(pq)
            res.append([x, y])
            
        return res