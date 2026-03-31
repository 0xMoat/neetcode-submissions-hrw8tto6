class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx_dic = {}
        for i, c in enumerate(s):
            last_idx_dic[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_idx_dic[c])

            if i == end:
                res.append(size)
                size = 0

        return res

