class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        res = 0

        for c in char_set:
            l = 0
            c_count = 0
            for r in range(len(s)):
                if s[r] == c:
                    c_count += 1

                while (r - l + 1) - c_count > k  and l < r:
                    if s[l] == c:
                        c_count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res