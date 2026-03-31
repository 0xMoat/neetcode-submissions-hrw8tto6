class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)

        prev2, prev1 = 1, 1
        for i in range(2, n+1):
            temp = 0
            if s[i-1] != "0":
                temp += prev1 
            
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                temp += prev2

            prev2, prev1 = prev1, temp

        return prev1


