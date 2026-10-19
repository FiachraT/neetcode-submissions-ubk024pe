class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        atl = set()
        pac = set()

        def dfs(r, c, visit_set):
            visit_set.add((r,c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0<= nc < cols and (nr, nc) not in visit_set and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visit_set)


        # go from borders
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)
        
        return list(pac & atl)

        