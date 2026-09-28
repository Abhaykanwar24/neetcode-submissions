class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n , 0 ) +1

        res = []
        for key , val in freq.items():
            if val > len(nums)//3 :
                res.append(key)
        

        return res