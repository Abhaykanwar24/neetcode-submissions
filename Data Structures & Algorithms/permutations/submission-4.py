class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []
        seen = set()


        def backtrack():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return

            for j in range(len(nums)):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                perms.append(nums[j])

                backtrack()
                seen.remove(nums[j])
                perms.pop()

        backtrack()

        return res
