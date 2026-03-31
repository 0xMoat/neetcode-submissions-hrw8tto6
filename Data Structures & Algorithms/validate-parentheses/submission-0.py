class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"[": "]", "{":"}", "(":")"}
        stack = []

        for c in s:
            if c in dic:
                stack.append(c)
            elif stack and dic[stack[-1]] == c:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0