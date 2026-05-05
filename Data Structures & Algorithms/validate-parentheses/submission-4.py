class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_dic = {")":"(","]":"[","}":"{"}

        for c in s:
            if c not in char_dic:
                stack.append(c)
            elif stack and stack[-1] == char_dic[c]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
            
