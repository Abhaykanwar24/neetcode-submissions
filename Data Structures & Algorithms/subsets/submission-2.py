class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        curset = []

        def DFS(i):
            if i >= len(nums):
                subset.append(curset.copy())
                return


            curset.append(nums[i])
            DFS(i+1)
            curset.pop()
            DFS(i+1)


        DFS(0)
        return subset
