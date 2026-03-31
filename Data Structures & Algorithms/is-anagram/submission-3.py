class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # time complexity O(n)
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        for k, v in counter_s.items():
            if k not in counter_t or counter_t[k] != v:
                return False
        return True