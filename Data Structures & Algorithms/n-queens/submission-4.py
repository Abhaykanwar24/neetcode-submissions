class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return


            for j in range(n):
                if j in col or (i+j) in posDiag or (i-j) in negDiag:
                    continue
                col.add(j)
                posDiag.add(i+j)
                negDiag.add(i-j)
                board[i][j] = "Q"

                backtrack(i+1)
                col.remove(j)
                posDiag.remove(i+j)
                negDiag.remove(i-j)
                board[i][j] = "."



        backtrack(0)

        return res
                 