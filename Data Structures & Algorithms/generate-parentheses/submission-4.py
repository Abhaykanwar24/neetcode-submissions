class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []


        def backtrack(OpenPar , ClosedPar):
            if OpenPar == ClosedPar == n:
                res.append("".join(stack))
                return 

            if OpenPar < n:
                stack.append("(")
                backtrack(OpenPar + 1 , ClosedPar)
                stack.pop()

            if ClosedPar < OpenPar:
                stack.append(")")
                backtrack(OpenPar , ClosedPar + 1)
                stack.pop()



        backtrack(0,0)

        return res