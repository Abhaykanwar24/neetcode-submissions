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
            if token in ops:
                b = stack.pop()   # right operand
                a = stack.pop()   # left operand
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))


        return stack[0]



        