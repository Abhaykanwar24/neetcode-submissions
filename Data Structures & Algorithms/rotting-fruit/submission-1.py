class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])
        queue = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visit.add(())
        minutes = 0
        while queue:
            for i in range(len(queue)):
                r , c = queue.popleft()

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr , dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or grid[nr][nc] != 1):
                        continue

                    grid[nr][nc] = 2
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))

            minutes +=1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1  


        return -1 if minutes-1 == 0 else minutes-1



