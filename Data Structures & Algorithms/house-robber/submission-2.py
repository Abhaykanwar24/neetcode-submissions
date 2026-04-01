class Solution:
    def rob(self, nums: List[int]) -> int:
        cost1= 0
        cost2 = 0
        for i in range(0 , len(nums) , 2):
            cost1 += nums[i]
        for i in range(1 , len(nums) , 2):
            cost2 += nums[i]

        return max(cost1 , cost2)