class Solution:
    def longestPalindrome2(self, s: str) -> str:
        res_idx, res_len = 0, 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > res_len:
                        res_len = j - i + 1
                        res_idx = i
            
        return s[res_idx:(res_len + res_idx)]

    def longestPalindrome(self, s):
        res_idx, res_len = 0, 0
        n = len(s)
        for i in range(n):
            # odd length
            # max traversal time is n/2
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res_idx = l
                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res_idx = l
                l -= 1
                r += 1

        return s[res_idx:res_idx+res_len]
        # time complexity is O(n^2),space complexity is O(1)

