class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int cur_sum = 0;
        int l = 0;
        int res = INT_MAX;
        for (int r = 0 ; r < nums.size(); r++){
            cur_sum += nums[r];

            while (cur_sum >= target){
                res = min(res , r - l +1);
                cur_sum -= nums[l];
                l+=1;
            }

        }
        return res == INT_MAX ? 0 : res; 
    }
};