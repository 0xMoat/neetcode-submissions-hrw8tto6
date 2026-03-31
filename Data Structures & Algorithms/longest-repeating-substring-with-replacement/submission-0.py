class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        res = 0

        for c in char_set:
            count = 0
            l = 0
            for r in range(len(s)):
                # move window right boundary
                if s[r] == c:
                    count += 1

                # move window left boundary
                while (r - l + 1) - count > k and l < r:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r- l + 1)
        return res