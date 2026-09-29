class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {}
        for i in range(len(s) - 1 , -1 , -1):
            if s[i] not in last_pos:
                last_pos[s[i]] = i

        res = []
        i = 0
        while i < len(s):
            intial_start = i
            start = i
            end = last_pos[s[i]]
           
            while start < end:
                if last_pos[s[start]] > end:
                    end = last_pos[s[start]]
                start +=1

            res.append(end - intial_start + 1)
            i = end + 1


        return res

