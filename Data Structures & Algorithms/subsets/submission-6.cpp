class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> subsets;
        vector<int> curset;
        DFS(0 , nums , curset , subsets);
        return subsets;    
    }
private:
    void DFS(int i , vector<int>& nums , vector<int>& curset , vector<vector<int>>& subsets ){
        if (i >= nums.size()){
            subsets.push_back(curset);
            return;
        }
        curset.push_back(nums[i]);
        DFS(i+1 , nums , curset , subsets);
        curset.pop_back();

        DFS(i+1 , nums ,curset , subsets);
    }
};
