class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        cur_set = []

        def backtrack(i):
            if i >= len(nums):
                subset.append(cur_set.copy())
                return

            cur_set.append(nums[i])
            backtrack(i+1)
            cur_set.pop()
            backtrack(i+1)


        
        backtrack(0)

        return subset