class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {')':'(' , ']' :'[' , '}' : '{'}

        stack = []
        

        for i in range(len(s)):
            if s[i] in par_dict:
                if stack and stack[-1] == par_dict[s[i]]:
                    stack.pop()
                else:
                    return False


            else:
                stack.append(s[i])



        return not stack



        