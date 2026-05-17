class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()
        while q or max_heap:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                left_count = 1 + heapq.heappop(max_heap)
                if left_count:
                    q.append([left_count, time+n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
                