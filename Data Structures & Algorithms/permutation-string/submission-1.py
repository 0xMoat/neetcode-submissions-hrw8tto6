import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = collections.Counter(s1)
        s1_len = len(s1)

        win_dic = collections.defaultdict(int)
        l = 0
        for r in range(len(s2)):
            # 遇到无关字符:窗口作废,左边界跳到 r+1,计数清零
            if s2[r] not in s1_dic:
                win_dic.clear()
                l = r + 1
                continue

            win_dic[s2[r]] += 1

            # 窗口超长,缩左边界
            if r - l + 1 > s1_len:
                win_dic[s2[l]] -= 1
                if win_dic[s2[l]] == 0:
                    del win_dic[s2[l]]
                l += 1

            if win_dic == s1_dic:
                return True

        return False