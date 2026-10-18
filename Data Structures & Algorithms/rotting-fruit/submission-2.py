class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #same type of problem as before
        # bfs on every rotten fruit cell
        # only have to return minimum nimber of minutes
        # keep count of fresh and subtract 1 when it goes wrotten, if count still greater than 1 by time all commecced are rotten return - 1

        fresh = 0
        q = deque()
        rows, cols = len(grid), len(grid[0])

        def addTile(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] != 0 and grid[r][c] != 2:
                q.append((r, c))
                grid[r][c] = 2
                nonlocal fresh
                fresh -= 1

        for r in range(rows):
            for c in range(cols):
                t = grid[r][c]
                if t == 1:
                    fresh +=1
                elif t == 2:
                    q.append((r, c))
        
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addTile(r+ 1, c)
                addTile(r - 1, c)
                addTile(r, c + 1)
                addTile(r, c - 1)
            time += 1

        
        if fresh != 0:
            return -1
        return time

                