class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len, res_idx = 0, 0
        n = len(s)

        for i in range(n):
            # odd
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res_len = (r - l + 1)
                    res_idx = l
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res_len = (r - l + 1)
                    res_idx = l
                l -= 1
                r += 1

        return s[res_idx:res_idx+res_len]