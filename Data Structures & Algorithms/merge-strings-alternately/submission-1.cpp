class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res;
        int l = 0  , r = 0;
        while (l < word1.size() && r < word2.size()){
            res += word1[l++];
            res += word2[r++];
        }
        res += word1.substr(l);
        res += word2.substr(r);
        return res;
    }
};