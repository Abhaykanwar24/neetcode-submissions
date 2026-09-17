class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float("-inf")

        cur_max = 0

        for n in nums:
            cur_max = max(cur_max + n , n)
            global_max = max(cur_max , global_max)


        return global_max