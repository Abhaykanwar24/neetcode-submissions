import operator
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b) if b != 0 else 0 
        }
        #ops['+'](a, b)
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                result = ops[token](a, b)
                stack.append(result)


        return stack[0]



        