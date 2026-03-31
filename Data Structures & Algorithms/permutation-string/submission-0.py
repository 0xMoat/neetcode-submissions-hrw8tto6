class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = collections.Counter(s1)
        s1_len = len(s1)

        l = 0
        win_dic = {c: 0 for c in s1}
        for r in range(len(s2)):
            if s2[r] in s1_dic:
                win_dic[s2[r]] += 1

            while (r - l + 1) > s1_len:
                if s2[l] in s1_dic:
                    win_dic[s2[l]] -= 1
                l += 1
            if s1_dic == win_dic:
                print(l,r,count,s2[l],s2[r])
                return True

        return False