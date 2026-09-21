class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []

        for i in range(len(s)):
            if s[i] == "*":
                star.append(i)
            elif s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while stack and star:
            if stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                return False

        return len(stack) == 0