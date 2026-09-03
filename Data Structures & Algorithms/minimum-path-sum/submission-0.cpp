class Solution {
public:
    int ROW;
    int COL;
    int minPathSum(vector<vector<int>>& grid) {
        ROW = grid.size();
        COL = grid[0].size();
        vector<vector<int>> dp(
            ROW,
            vector<int>(COL, -1)
        );
        return DFS(0 , 0 , grid , dp);
    }

private:
    int DFS(int i , int j , vector<vector<int>>& grid ,vector<vector<int>>& dp ){
        if (i == ROW -1 && j == COL - 1) return grid[i][j];
        if(i < 0 || j < 0 || i >= ROW || j >= COL){
            return INT_MAX;
        }
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        int sum = grid[i][j];
        sum += min(
            DFS(i + 1, j, grid , dp),
            DFS(i, j + 1, grid , dp)
        );

        dp[i][j] = sum;


        return dp[i][j];
    } 
};