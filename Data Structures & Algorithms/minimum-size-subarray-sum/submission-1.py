class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        minimum = float('inf')
        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                minimum = min(minimum, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if minimum == float('inf') else minimum
            

            

            