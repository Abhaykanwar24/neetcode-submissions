class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []

        def backtrack(start):
            if start == len(s):
                res.append(pal.copy())
                return

            for end in range(start, len(s)):
                if self.isPal(s, start, end):
                    pal.append(s[start:end+1])
                    backtrack(end+1)
                    pal.pop()

        backtrack(0)
        return res

    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True


