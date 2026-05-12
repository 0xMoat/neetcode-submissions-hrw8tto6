class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = collections.Counter(s1)
        win_dic = {c:0 for c in s1}

        l = 0
        for r in range(len(s2)):
            if s2[r] in s1_dic:
                win_dic[s2[r]] += 1
            
            while r - l + 1 > len(s1):
                if s2[l] in s1_dic:
                    win_dic[s2[l]] -= 1
                l += 1
            
            if s1_dic == win_dic:
                return True
        return False