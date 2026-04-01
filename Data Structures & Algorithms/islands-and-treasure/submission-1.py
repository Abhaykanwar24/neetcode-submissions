class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW , COL = len(grid) , len(grid[0])
        queue = deque()
        INF = 2147483647
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nc < 0 or nr >= ROW or nc >= COL or
                    grid[nr][nc] != INF):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))

            

