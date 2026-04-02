class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.pq = []
        for s in stones:
            heapq.heappush(self.pq, -s)

        while len(self.pq) > 1:
            s1 = heapq.heappop(self.pq) 
            s2 = heapq.heappop(self.pq)
            if s1 == s2:
                continue
            else:
                heapq.heappush(self.pq, s1 - s2)

        return -self.pq[0] if len(self.pq) > 0 else 0

