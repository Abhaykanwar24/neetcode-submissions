class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> curset;
        DFS(1 ,n ,k , curset , res);
        return res;
        
    }
private:
    void DFS(int i ,int n , int k , vector<int>& curset , vector<vector<int>>& res){
        if (curset.size() == k){
            res.push_back(curset);
            return;
        }
        if (i > n){
            return;
        }
        curset.push_back(i);
        DFS(i +1 ,n,k , curset , res);
        curset.pop_back();

        DFS(i +1 ,n ,k , curset , res);
    }
};