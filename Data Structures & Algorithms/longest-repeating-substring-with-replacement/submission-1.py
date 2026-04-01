class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r=0
        limit = 0
        longest = 0
        while r  < len(s):
            if s[l] != s[r]:
                if limit < k :
                    r+=1
                else:
                    l = r
                    limit = 0
            else :
                r+=1
                cur_longest = (r-l) 
                longest = max(longest , cur_longest)


        return longest

                

            
            

        