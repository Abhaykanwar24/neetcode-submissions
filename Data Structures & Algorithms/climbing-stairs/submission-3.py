class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        dp =  [1,1]
        i = 2
        for _ in range(2, n+1):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp

        return dp[1]