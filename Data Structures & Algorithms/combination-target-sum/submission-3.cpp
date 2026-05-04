class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> curset;
        vector<vector<int>> comb;
        DFS(0 ,0 ,  target , nums , curset , comb);
        return comb;
    }

private:
    void DFS(int i ,int sum, int target , vector<int>& nums , vector<int>& curset , vector<vector<int>>& comb){
        if ( sum == target){
            comb.push_back(curset);
            return;
        }
        if ( i >= nums.size() || sum > target){
            return;
        }
        curset.push_back(nums[i]);
        DFS(i , nums[i] + sum , target , nums, curset,comb);
        curset.pop_back();

        DFS(i+1 , sum , target , nums, curset,comb);

    }
};
