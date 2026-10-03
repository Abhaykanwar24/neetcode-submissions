class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        res = 0
        freq = {0:1}

        for i in range(len(nums)):
            prefix += nums[i]
            diff = prefix - k

            if diff in freq:
                res += freq[diff]
            
            freq[prefix] = freq.get(prefix , 0 ) + 1

        return res