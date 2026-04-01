class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        subset_sum = []
        curset_sum = []

        def DFS(i , Tsum):
            if Tsum == target:
                subset_sum.append(curset_sum.copy())
                return
            if i>=len(nums):
                return
            if Tsum > target:
                return

            curset_sum.append(nums[i])
            DFS(i+1 , Tsum + nums[i])
            curset_sum.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            DFS(i+1 , Tsum) 

        DFS(0,0)
        return subset_sum

