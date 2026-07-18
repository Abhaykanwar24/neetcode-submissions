class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> front(n);
        vector<int> back(n);
        front[0] = 1;
        back[n - 1] = 1;
        for (int i = 1 ; i < nums.size() ; i++){
            front[i] = front[i-1] * nums[i-1];
        }
        for (int i = nums.size() - 2 ; i >=0 ; i--){
            back[i] = back[i+1] * nums[i+1];
        }

        vector<int> res(nums.size());

        for (int i = 0; i < n; i++) {
        res[i] = front[i] * back[i];
        }
        return res;

    }
};
