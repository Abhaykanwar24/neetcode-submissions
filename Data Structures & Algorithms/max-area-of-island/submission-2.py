class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [[1,0] , [-1,0] , [0,1] , [0,-1]]
        ROW , COL = len(grid) , len(grid[0])
        seen = set()

        def DFS(r,c):
            if (min(r,c) < 0  or r >= ROW or c >= COL or 
                grid[r][c] == 0 or (r, c) in seen):
                return 0

            seen.add((r, c))
            area = 1

            for dr, dc in direction:
                area += DFS(r + dr, c + dc)

            return area

        max_island = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in seen:
                    max_island = max(max_island, DFS(r, c))
    
            
        return max_island
