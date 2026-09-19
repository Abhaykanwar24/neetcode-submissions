class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in count:
                count[s[i]] = i


        l = 0

        window = []
        
        while l < len(s):
            r = count[s[l]]
            i = l
            while i <= r:
                r = max(r, count[s[i]])
                i += 1
            
            window.append(r - l +1)
            l = r + 1


        return window
            