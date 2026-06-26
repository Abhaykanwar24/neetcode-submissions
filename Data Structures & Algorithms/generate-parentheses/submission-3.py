class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(OpenN , ClosedN):
            if OpenN == ClosedN == n:
                res.append("".join(stack))
                return


            if OpenN < n:
                stack.append("(")
                backtrack(OpenN + 1 , ClosedN)
                stack.pop()

            if ClosedN < OpenN:
                stack.append(")")
                backtrack(OpenN , ClosedN + 1)
                stack.pop()


        backtrack(0,0)

        return res