class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        t_len = len(t)
        window = {c: 0 for c in t}

        l, r = 0, 0
        valid = 0
        start, res_length = 0, float('inf')
        while r < len(s):
            if s[r] in need:
                window[s[r]] += 1
                if window[s[r]] == need[s[r]]:
                    valid += 1 

            while valid == len(need):
                if (r - l + 1) < res_length:
                    res_length = r - l + 1
                    start = l
                if s[l] in need:
                    if window[s[l]] == need[s[l]]:
                        valid -= 1
                    window[s[l]] -= 1
                l += 1

            r += 1
                
        return "" if res_length == float('inf') else s[start:start + res_length]

