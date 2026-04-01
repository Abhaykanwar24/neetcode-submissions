class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t , window = {} , {}

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1


        l = 0 
        have , need = 0 ,  len(count_t)
        res , reslen = [-1 , -1] , float("inf")
        for r in range(len(s)):
            window[s[r]] = window.get(s[r] , 0 ) +1

            if s[r] in count_t and count_t[s[r]]  == window[s[r]]:
                have+=1

            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)

                window[s[l]] -= 1
                
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have-=1

                l+=1

        l ,r = res
        return s[l:r+1] if reslen != float("inf") else ""

                










