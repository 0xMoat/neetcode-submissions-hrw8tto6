class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # time complexity O(n+m), space is O(1) casue just need constant number keys
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)

        return counter_s == counter_t

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False
        return True