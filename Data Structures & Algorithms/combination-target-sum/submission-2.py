class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combs = []
        def DFS(i,tsum):
            if tsum == target:
                res.append(combs.copy())
                return
            if i >=len(nums):
                return
            if tsum > target:
                return

            combs.append(nums[i])
            DFS(i , tsum+nums[i])
            combs.pop()
            DFS(i+1 , tsum)


        DFS(0,0)
        return res
