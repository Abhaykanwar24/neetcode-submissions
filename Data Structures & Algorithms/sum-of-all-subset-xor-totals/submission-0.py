class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def DFS(i,total):
            if i == len(nums):
                return total

            # include nums[i]
            return DFS(i+1 , total ^ nums[i]) +  DFS(i+1 , total)



        return DFS(0,0)
                