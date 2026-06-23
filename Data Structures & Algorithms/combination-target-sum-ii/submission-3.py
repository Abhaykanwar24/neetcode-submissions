class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        nums.sort()
        def backtrack(i , total):
            if total == target:
                res.append(comb.copy())
                return

            if total > target or i >= len(nums):
                return

            comb.append(nums[i])
            backtrack(i+1 , total + nums[i])
            comb.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            backtrack(i+1 , total)


        backtrack(0,0)

        return res