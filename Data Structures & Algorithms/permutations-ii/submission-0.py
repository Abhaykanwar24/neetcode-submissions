class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []
        nums.sort()
        used = [False] * len(nums)


        def backtrack():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return


            for j in range(len(nums)):
                if used[j]:
                    continue
                if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                    continue
                used[j] = True
                perms.append(nums[j])
                backtrack()
                used[j] = False
                perms.pop()



        backtrack()

        return res