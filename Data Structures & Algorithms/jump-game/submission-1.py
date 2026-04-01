class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        i = 0
        n = len(nums)

        while i < n and nums[i] != 0:
            i = i + nums[i]
            if i == n - 1:
                return True


        return False