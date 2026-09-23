class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        res = [1]
        prefix = 1
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            res.append(prefix)

        postfix = 1
        for i in range(len(nums)-1 , -1 ,-1):
            res[i] *= postfix
            postfix *= nums[i]


        return res            