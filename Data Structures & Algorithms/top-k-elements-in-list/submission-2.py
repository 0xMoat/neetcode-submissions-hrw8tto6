class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        for i,v in counter.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq)-1, 0, -1):
            while freq[i] and k:
                f = freq[i].pop()
                res.append(f)
                k -= 1
                if k == 0:
                    return res
        return res