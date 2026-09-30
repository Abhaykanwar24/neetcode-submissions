class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        cur_set = []

        def backtrack(i, curSum):
            if curSum == target:
                comb.append(cur_set.copy())
                return

            if i >= len(nums) or curSum > target:
                return

            cur_set.append(nums[i])
            backtrack(i, curSum + nums[i])
            cur_set.pop()

            backtrack(i + 1, curSum)

        backtrack(0, 0)

        return comb