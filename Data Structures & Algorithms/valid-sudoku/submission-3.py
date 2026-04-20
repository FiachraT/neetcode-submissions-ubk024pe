class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r, s in enumerate(board):
            for c, d in enumerate(s):
                if d == ".":
                    continue
                
                if d in row[r] or d in column[c] or d in square[r // 3, c //3]:
                    return False
                
                row[r].add(d)
                column[c].add(d)
                square[r //3, c // 3].add(d)
        return True