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

            combs.append(i)
            DFS(i+1)
            combs.pop()
            DFS(i+1)

        DFS(1)
        return res


             