class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        mul = 1
        for i in range(len(nums)):
            prefix[i] = mul
            mul *= nums[i]

        postfix = [1] * len(nums)
        mul =1
        for i in range(len(nums)-1 , -1 ,-1):
            postfix[i] = mul
            mul *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])

        return res

        

        