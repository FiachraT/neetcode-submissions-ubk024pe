from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs
        # traverse from each land cell or each treasure chest?
        #bfs traverse from all treasure chests at the same time
        # do that by appending all treasure chests to queue then bfs
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def addSquare(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] != -1 and (r,c) not in visited:
                q.append((r, c))
                visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    print(r,c)
                    q.append((r,c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addSquare(r + 1, c)
                addSquare(r - 1, c)
                addSquare(r, c + 1)
                addSquare(r, c - 1)
            dist +=1
        









        
        

        