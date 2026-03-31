class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # maximum frequent is len(nums), its index in freq array is len(nums) + 1
        # freq[0] is a dumb item
        # 这正是桶排序的核心动作——不做比较，直接把元素放到"它该在的位置"。频率就是桶的编号，放进去就完成了"排序"。
        freq = [[] for _ in range(len(nums) + 1)] 
        counter_dic = collections.defaultdict(int)
        for n in nums:
            counter_dic[n] += 1
        for n, c in counter_dic.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res

        return res