class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for n in s:
            if n not in hash_s:
                hash_s[n] = 1
            hash_s[n] +=1

        for n in t:
            if n not in hash_t:
                hash_t[n] = 1
            hash_t[n] +=1


        return hash_s == hash_t
        


        