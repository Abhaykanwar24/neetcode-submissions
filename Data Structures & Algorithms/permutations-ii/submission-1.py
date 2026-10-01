class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        cur_perm = []
        nums.sort()
        seen = set()
        def backtrack():
            if len(cur_perm) == len(nums):
                perms.append(cur_perm.copy())
                return

            for j in range(len(nums)):
                if j in seen:
                    continue

                if j > 0 and nums[j] == nums[j - 1] and j - 1 not in seen:
                    continue

                seen.add(j)
                cur_perm.append(nums[j])

                backtrack()

                cur_perm.pop()
                seen.remove(j)

        backtrack()

        return perms