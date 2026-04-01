class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in look:
                return [look[diff] , i]

            look[nums[i]] = i
        