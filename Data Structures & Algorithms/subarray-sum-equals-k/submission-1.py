class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        cnt = 0
        prefix_sum = {0:1}

        for n in nums:
            preSum += n
            diff = preSum - k

            if diff in prefix_sum:
                cnt += prefix_sum[diff]

            prefix_sum[preSum]= prefix_sum.get(preSum , 0 ) + 1


        return cnt