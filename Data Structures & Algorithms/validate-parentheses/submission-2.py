class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"[": "]", "{":"}", "(":")"}
        stack = []

        for c in s:
            if c in dic:
                stack.append(c)
            elif stack and c == dic[stack[-1]]:
                    stack.pop()
            else:
                return False
        return True if not stack else False