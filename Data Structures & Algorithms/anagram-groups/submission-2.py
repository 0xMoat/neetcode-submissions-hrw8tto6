class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_dic = collections.defaultdict(list)
        for s in strs:
            counter = [0]*26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            counter_dic[tuple(counter)].append(s)

        return list(counter_dic.values())