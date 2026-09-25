class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        res = ""
        while l < len(word1) and r < len(word2):
            if l <= r:
                res += word1[l]
                l+=1
            else:
                res += word2[r]
                r+=1

        while l < len(word1):
            res += word1[l]
            l+=1
        while r < len(word2):
            res += word2[r]
            r +=1



        return res