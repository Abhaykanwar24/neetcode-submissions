class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        i = 0
        n = len(nums)

        while i < n and nums[i] != 0:
            max_jump = i + nums[i]
            max_val = 0
            for j in range(i , max_jump):
                max_val = max(nums[j] , max_val)
            i = i + max_val
            if i == len(nums) - 1:
                return True

        return False