class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs for maximum area
        count = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        max_count = 0

        def dfs(r: int, c: int) -> int:
            stack = []
            stack.append((r,c))
            count = 1
            grid[r][c] = 0

            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        count +=1
                        grid[nr][nc] = 0
                        stack.append((nr, nc))
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = dfs(r, c)
                    max_count = max(count, max_count)
        return max_count

        