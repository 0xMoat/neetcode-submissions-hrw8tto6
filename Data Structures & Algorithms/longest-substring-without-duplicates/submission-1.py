class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in record:
                record.remove(s[l])
                l += 1
            record.add(s[r])
            res = max(res, r - l + 1)
        return res