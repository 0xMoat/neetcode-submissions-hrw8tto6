class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, -s)

        while len(max_heap) > 1:
            heaviest1 = - heapq.heappop(max_heap)
            heaviest2 = - heapq.heappop(max_heap)

            if heaviest1 - heaviest2 > 0:
                heapq.heappush(max_heap, heaviest2 - heaviest1)
            
        return 0 if len(max_heap) == 0 else -max_heap[0]


