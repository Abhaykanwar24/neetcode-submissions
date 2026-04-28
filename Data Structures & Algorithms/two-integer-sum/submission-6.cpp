class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map < int , int > ind;
        for (int i = 0 ; i < nums.size() ; i ++){
            ind[nums[i]] = i;
        }
        for (int i = 0 ; i < nums.size(); i++){
            int diff = target - nums[i];
            if( ind.count(diff) && ind[diff] != i){
                return {i , ind[diff]};
            }
        }
        return {};
    }
};
