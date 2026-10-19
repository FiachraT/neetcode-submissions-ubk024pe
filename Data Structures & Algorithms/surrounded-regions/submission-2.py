class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # forward way of thinking: for each o, do a dfs to see if it can be captured or not
        # reverse way of thinking: capture everything except uncapturable regions
        #reverse is more efficient
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            board[r][c] = "T"
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    dfs(nr, nc)
        
        edge = cols - 1
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][edge] == "O":
                dfs(r, edge)
        
        edge = rows - 1
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[edge][c] == "O":
                dfs(edge, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


        