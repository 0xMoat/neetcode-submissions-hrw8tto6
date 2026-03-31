class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        for s in stones:
            heapq.heapify(heap)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if b > a:
                heapq.heappush(heap, a - b)
        return 0 if len(heap) == 0 else -heapq.heappop(heap)

        