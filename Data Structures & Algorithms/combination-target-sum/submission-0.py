class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curComb = []

        def DFS(i, curSum):
            if curSum == target:
                res.append(curComb.copy())
                return

            if i >= len(nums) or curSum > target:
                return

            curComb.append(nums[i])
            DFS(i, curSum + nums[i])
            curComb.pop()

            DFS(i + 1, curSum)

        DFS(0, 0)
        return res

        