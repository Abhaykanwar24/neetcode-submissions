class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW , COL = len(grid) , len(grid[0])
        queue = deque()
        INF = 2147483647
        
        def bfs(r,c):
            queue = deque()
            queue.append((r, c))
            visit = set()
            visit.add((r,c))
            length = 0
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return length

                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        if (min(r + dr, c + dc) < 0 or
                            r + dr == ROW or c + dc == COL or
                            (r + dr, c + dc) in visit or grid[r + dr][c + dc] == -1):
                            continue

                        queue.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                length += 1

            return length
            

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)

