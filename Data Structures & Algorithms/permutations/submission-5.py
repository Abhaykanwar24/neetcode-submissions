class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_perm = []
        seen = set()

        def backtrack():
            if len(cur_perm) == len(nums):
                res.append(cur_perm.copy())
                return

            for j in range(len(nums)):
                if nums[j] in seen:
                    continue

                seen.add(nums[j])
                cur_perm.append(nums[j])

                backtrack()

                seen.remove(nums[j])
                cur_perm.pop()


        backtrack()

        return res
