class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or strs[0][i] != string[i]:
                    return string[:i]
        return strs[0]