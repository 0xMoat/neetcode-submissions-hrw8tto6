class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity: m * n
        # space complexity: m
        counters_dic = collections.defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            counters_dic[tuple(counter)].append(s)
        return list(counters_dic.values())