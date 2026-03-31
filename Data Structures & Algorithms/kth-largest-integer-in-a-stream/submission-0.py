class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.heap = nums.copy()
        heapq.heapify(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.kth, self.heap)[-1]
