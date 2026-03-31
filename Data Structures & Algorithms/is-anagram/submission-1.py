class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic, t_dic = {}, {}
        for i in range(len(s)):
            s_dic[s[i]] = s_dic[s[i]] + 1 if s[i] in s_dic else 0
            t_dic[t[i]] = t_dic[t[i]] + 1 if t[i] in t_dic  else 0
        return s_dic == t_dic