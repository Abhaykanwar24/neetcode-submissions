class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        curComb = []
        def DFS_Comb(i):
            if len(curComb) == k:
                comb.append(curComb.copy())
                return

            if i > n:
                return

            for j in range(i , n +1 ):
                curComb.append(j)
                DFS_Comb(j+1)
                curComb.pop()

        DFS_Comb(1)
        return comb
             