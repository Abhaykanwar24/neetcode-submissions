class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen  = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in seen :
                seen.remove(s[l])
                l+=1

            seen.add(s[r])

            cur_longest = (r-l) + 1
            longest = max(longest,cur_longest)


        return longest 
        