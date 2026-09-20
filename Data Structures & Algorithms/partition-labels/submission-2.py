class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in range(len(s)-1 , -1 ,-1):
            if s[i] not in last_index:
                last_index[s[i]] = i

        l = 0
        r = 0
        
        windows = []
        while  l < len(s):
            r = last_index[s[l]]
            i = l
            while i <= r:
                if last_index[s[i]] > r:
                    r = last_index[s[i]]
                i+=1
            windows.append(r-l+1)
            l = r + 1   
            



        return windows


            

            

