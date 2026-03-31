class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root 
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
        cur_node.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.endOfWord
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            elif c in node.children:
                return dfs(i+1, node.children[c])
            else:
                return False

        return dfs(0, self.root)








