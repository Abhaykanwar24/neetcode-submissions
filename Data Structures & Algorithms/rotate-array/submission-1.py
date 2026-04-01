class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = 0
        r = len(nums)-k

        while r < len(nums) :
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r+=1

        