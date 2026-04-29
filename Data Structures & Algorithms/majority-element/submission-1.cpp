class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map < int , int > count;
        int max = 0 , max_count = 0;

        for ( int num : nums){
            count[num]++;
            if (count[num] > max_count){
                max = num;
                max_count = count[num];
            }
        }
        return max;
        

    }
};