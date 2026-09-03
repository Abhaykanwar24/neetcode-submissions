class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(
            m,
            vector<int>(n, -1)
        );

        return DFS(0, 0, m, n, dp);
    }

private:
    int DFS(int i, int j, int m, int n, vector<vector<int>>& dp){
        if(i == m - 1 && j == n - 1) return 1;

        if(i < 0 || j < 0 || i >= m || j >= n){
            return 0;
        }

        if(dp[i][j] != -1){
            return dp[i][j];
        }

        int count = 0;

        count += DFS(i + 1, j, m, n, dp)
              + DFS(i, j + 1, m, n, dp);

        dp[i][j] = count;

        return dp[i][j];
    }
};