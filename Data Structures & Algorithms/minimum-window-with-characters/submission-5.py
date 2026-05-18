class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        win = {c:0 for c in t}

        l = 0
        res_begin, res_len = 0, float('inf')
        vaild_c = 0
        for r in range(len(s)):
            if s[r] in need:
                win[s[r]] += 1
                if win[s[r]] == need[s[r]]:
                    vaild_c += 1

            while vaild_c == len(need):
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_begin = l

                if s[l] in win:
                    if win[s[l]] == need[s[l]]:
                        vaild_c -= 1
                    win[s[l]] -= 1
                l += 1
        
        return "" if res_len == float('inf') else s[res_begin:res_begin+res_len]