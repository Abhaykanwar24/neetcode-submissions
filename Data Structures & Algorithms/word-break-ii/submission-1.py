class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = [-1] * len(s)

        def backtrack(i):
            if i == len(s):
                return [""]

            if memo[i] != -1:
                return memo[i]

            res = []

            for j in range(i, len(s)):
                w = s[i:j + 1]

                if w in wordDict:
                    suffixes = backtrack(j + 1)

                    for suffix in suffixes:
                        if suffix:
                            res.append(w + " " + suffix)
                        else:
                            res.append(w)

            memo[i] = res
            return res

        return backtrack(0)