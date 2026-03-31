class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create a dictionary of sets. If string in set return False. If all pass return true. Ignore "."
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                if d in rows[r] or d in cols[c] or d in square[(r//3, c//3)]:
                    return False
                
                rows[r].add(d)
                cols[c].add(d)
                square[(r //3, c // 3)].add(d)
        return True
