class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_checker = collections.defaultdict(set)
        col_checker = collections.defaultdict(set)
        grid_checker = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    n = int(board[i][j])
                    if n in row_checker[i] or \
                    n in col_checker[j] or \
                    n in grid_checker[(i//3, j //3)]:
                        return False

                    row_checker[i].add(n)
                    col_checker[j].add(n)
                    grid_checker[(i//3, j //3)].add(n)
        return True