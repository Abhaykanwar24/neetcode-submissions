class Solution:
    def countSubstrings(self, s: str) -> int:
        def check_pali(l , r):
            count = 0 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count +=1
                r +=1
                l-=1

            return count

        total = 0
        for i in range(len(s)):
            total += check_pali(i, i)
            total += check_pali(i, i+1)

        return total
