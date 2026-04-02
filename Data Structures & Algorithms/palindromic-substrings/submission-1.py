class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            # odd
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res