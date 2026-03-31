class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check_dic = collections.defaultdict(set)
        col_check_dic = collections.defaultdict(set)
        grid_check_dic = collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    temp = int(board[r][c])
                    if temp in row_check_dic[r] or \
                    temp in col_check_dic[c] or \
                    temp in grid_check_dic[(r//3, c//3)]:
                        return False
                        
                    row_check_dic[r].add(temp)
                    col_check_dic[c].add(temp)
                    grid_check_dic[(r//3, c//3)].add(temp)
        return True
