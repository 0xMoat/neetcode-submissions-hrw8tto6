class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = ''
        for c in s:
            if c.isalnum():
                reverse_s += c.lower()
        return reverse_s == reverse_s[::-1]