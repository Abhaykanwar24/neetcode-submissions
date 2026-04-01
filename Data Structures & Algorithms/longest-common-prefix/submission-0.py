class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        res = ""
        for s in range(1,len(strs)):
            for c in range(min(len(prefix), len(strs[s]))): 
                if prefix[c] == strs[s][c]:    
                    res += prefix[c]          
                else:
                    break

            prefix = res   
            res = ""   

        return prefix





        
        
        