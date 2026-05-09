class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        counter_dic_s = collections.Counter(s)
        counter_dic_t = collections.Counter(t)
        return counter_dic_s == counter_dic_t

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        checker = [0]*26
        for i in range(len(s)):
            checker[ord(s[i])-ord('a')] += 1
            checker[ord(t[i])-ord('a')] -= 1
        for c in checker:
            if c != 0:
                return False
        return True