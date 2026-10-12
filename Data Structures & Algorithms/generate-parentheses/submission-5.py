class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        cur = []
        def backtrack(openbrac , closedbrac):
            if openbrac == closedbrac == n:
                res.append("".join(cur))
                return

            if openbrac < n:
                cur.append("(")
                backtrack(openbrac + 1 , closedbrac)
                cur.pop()

            if closedbrac < openbrac:
                cur.append(")")
                backtrack(openbrac  , closedbrac + 1)
                cur.pop()

        backtrack(0 , 0)

        return res
