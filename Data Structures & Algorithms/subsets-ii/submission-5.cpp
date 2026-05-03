class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin() , nums.end());
        vector<int> curset;
        vector<vector<int>> subsets;
        DFS(0 , nums , curset , subsets);
        return subsets;
        
    }
private:
    void DFS(int i  , vector<int>& nums , vector<int>& curset , vector<vector<int>>& subsets){
        if ( i >= nums.size()){
            subsets.push_back(curset);
            return;
        }
        curset.push_back(nums[i]);
        DFS(i + 1 , nums , curset , subsets);
        curset.pop_back();

        while ( i+1 <= nums.size() && nums[i] == nums[i+1] ){
            i+=1;
        }
        DFS(i + 1 , nums , curset , subsets);
        
        }
};
