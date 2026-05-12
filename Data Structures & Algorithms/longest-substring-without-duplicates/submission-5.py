class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            # abcbb
            while s[r] in check_set:
                check_set.remove(s[l])
                l += 1
            check_set.add(s[r])
            res = max(res, r - l + 1)
        return res