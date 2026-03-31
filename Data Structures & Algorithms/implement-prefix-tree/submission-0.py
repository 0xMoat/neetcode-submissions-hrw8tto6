class PrefixTree:

    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        cur_dic = self.dic
        for c in word:
            if c not in cur_dic:
                cur_dic[c] = {}
            cur_dic = cur_dic[c]
        cur_dic["isWord"] = "YES"

    def search(self, word: str) -> bool:
        cur_dic = self.dic
        for c in word:
            print(word, cur_dic)
            if c not in cur_dic:
                return False
            cur_dic = cur_dic[c]
        return "isWord" in cur_dic


    def startsWith(self, prefix: str) -> bool:
        cur_dic = self.dic
        for c in prefix:
            if c not in cur_dic:
                return False
            cur_dic = cur_dic[c]
        return True