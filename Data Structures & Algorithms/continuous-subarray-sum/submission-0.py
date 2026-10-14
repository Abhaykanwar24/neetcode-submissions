class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0:-1}
        prefix = 0

        for i,n in enumerate(nums):
            prefix += n
            remainder = prefix % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i



        return False