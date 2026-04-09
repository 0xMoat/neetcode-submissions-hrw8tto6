class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = MinHeap()
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.min_heap.peek() is None or len(self.min_heap.heap) < self.k:
            self.min_heap.push(val)
        elif val > self.min_heap.peek():
            self.min_heap.pop()
            self.min_heap.push(val)
        return self.min_heap.peek()
        
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._sift_down(0)
        return val

    def peek(self) -> int:
        return self.heap[0] if self.heap else None

    def _sift_up(self, idx: int):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx: int):
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]