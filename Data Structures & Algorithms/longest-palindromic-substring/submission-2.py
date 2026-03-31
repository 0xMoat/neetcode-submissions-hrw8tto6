class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = 1
        res = s[0]
        for i in range(len(s)+1):
            for j in range(i+1):
                print(s[j:i])
                print(m, j, i, i - j)
                if s[j:i] == s[j:i][::-1] and (i - j) > m:
                    m = i - j
                    res = s[j:i]

        return res