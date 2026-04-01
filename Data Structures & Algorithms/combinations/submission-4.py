class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combs = []
        def DFS(i):
            if len(combs) == k:
                res.append(combs.copy())
                return

            if i > n:
                return

            for j in range(i , n+1):
                combs.append(j)
                DFS(j+1)
                combs.pop()

        DFS(1)
        return res


             