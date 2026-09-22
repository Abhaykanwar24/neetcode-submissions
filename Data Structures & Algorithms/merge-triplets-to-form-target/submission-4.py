class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False , False ,False]

        for a , b , c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]:
                    res[0] = True
                if b == target[1]:
                    res[1] = True
                if c == target[2]:
                    res[2] = True


        return all(res)