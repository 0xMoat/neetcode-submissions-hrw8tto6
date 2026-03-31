class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        return heapq.nlargest(self.kth, self.minHeap)[-1]
