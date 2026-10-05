class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_pali(l , r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1


            return True
        

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if check_pali(l+1 , r) or check_pali(l , r-1):
                    return True
                else:
                    return False
                
           
            l+=1
            r-=1

        
        return True
            