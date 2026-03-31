class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.isAlpha(s[r]) and l < r:
                print("r,",r,s[r])
                r -= 1
            while not self.isAlpha(s[l]) and l < r:
                print(l,s[l])

                l += 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isAlpha(self, c):
        if ord("A") <= ord(c) <= ord("Z") or \
            ord("a") <= ord(c) <= ord("z") or \
            ord("0") <= ord(c) <= ord("9"):
            return True
        return False