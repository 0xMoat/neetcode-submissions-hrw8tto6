class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_dic_s = collections.Counter(s)
        counter_dic_t = collections.Counter(t)
        return counter_dic_s == counter_dic_t