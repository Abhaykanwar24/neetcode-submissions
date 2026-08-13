class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();

        if (n == 1) {
            return nums[0];
        }

        return max(
            solve(0, n - 2, nums),
            solve(1, n - 1, nums)
        );
    }

private:
    int solve(int start, int n, vector<int>& nums) {
        vector<int> dp(n + 3 ,0);

        for (int i = n; i >= start; i--) {
            int rob = nums[i] + dp[i + 2];
            int skip = dp[i + 1];

            dp[i] = max(rob, skip);
        }

        return dp[start];
    }
};