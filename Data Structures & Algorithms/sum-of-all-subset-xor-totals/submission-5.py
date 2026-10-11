class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtrack(i , res):
            if i >= len(nums):
                return res

            take = backtrack(i + 1 , res ^ nums[i])
            skip = backtrack(i+1 , res)

            return take + skip


        return backtrack(0 , 0)

            