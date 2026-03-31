class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 建树部分保持不变
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        res = []

        # 修改 DFS：传入当前节点的父节点 parent，以便执行 pop
        def dfs(r, c, parent):
            char = board[r][c]
            if char not in parent.children:
                return

            curr_node = parent.children[char]
            
            # 找到单词
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None # 标记已找到，防止重复

            # 标记已访问
            board[r][c] = "#"
            
            # 递归探索
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    # 注意：这里如果 curr_node 已经被剪枝删空了，循环内也不会继续深入
                    dfs(nr, nc, curr_node)
            
            # 回溯：还原现场
            board[r][c] = char

            # --- 核心剪枝逻辑 ---
            # 如果当前节点没有子节点了，且它本身也不是某个单词的结尾
            # 说明这条路径已经“搜干抹净”了，直接从父节点中移除
            if not curr_node.children and not curr_node.word:
                parent.children.pop(char)

        # 遍历起点
        for r in range(ROWS):
            for c in range(COLS):
                # 只有当 root 有子节点时才继续，如果 root 被剪枝掏空了，搜索提前结束
                if root.children:
                    dfs(r, c, root)
        
        return res