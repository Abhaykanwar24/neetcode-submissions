class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin() , candidates.end());
        vector<vector<int>> res;
        vector<int> curcomb;
        DFS(0 , 0 ,target ,candidates,  curcomb , res);
        return res;
    }

private:
    void DFS(int i , int sum , int target ,vector<int>& nums ,  vector<int>& curcomb , vector<vector<int>>& res){
        if (sum == target){
            res.push_back(curcomb);
            return;
        }
        if (sum > target || i >= nums.size() ){
            return;
        }

        curcomb.push_back(nums[i]);
        DFS(i+1 , sum + nums[i] , target , nums , curcomb , res);

        while (i + 1< nums.size() && nums[i] == nums[i + 1] ){
            i++;
        }
        curcomb.pop_back();
        DFS(i+1 , sum  , target , nums , curcomb , res);
    }
};
