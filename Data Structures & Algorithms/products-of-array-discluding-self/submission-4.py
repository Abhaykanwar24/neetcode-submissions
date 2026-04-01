class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1]
        prod = 1
        for i in range(n - 1):
            prod *= nums[i]
            result.append(prod)

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]


        return result    
            


        

