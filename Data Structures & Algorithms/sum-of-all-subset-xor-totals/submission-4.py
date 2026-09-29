class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        

        def backtrack(i , xorSum):
            if i >= len(nums):
                return xorSum


            include = backtrack(i+1 , xorSum ^ nums[i])
            skip = backtrack(i+1 , xorSum)

            return include + skip



        return backtrack(0,0)