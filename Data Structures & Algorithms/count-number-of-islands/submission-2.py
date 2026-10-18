# last completed in 8 minutes

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1] , [0, 1]]
        visited = set()


        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                    dfs(nr, nc)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands
        