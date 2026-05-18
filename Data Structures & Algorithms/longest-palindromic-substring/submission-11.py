class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_begin, res_len = 0, 0
        n = len(s)

        for i in range(n):
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res_begin = l
                    res_len = r - l + 1
                l -= 1
                r += 1

            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res_begin = l
                    res_len = r - l + 1
                l -= 1
                r += 1

        return s[res_begin:res_begin+res_len]

