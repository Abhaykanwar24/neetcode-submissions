class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights) , sum(weights)
        res = r

        while l<=r:
            m = (l+r) // 2
            ships = 1
            curr = 0

            for w in weights:
                if curr + w > m:
                    ships +=1
                    curr = 0
                curr += w


            if ships > days:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res
                               