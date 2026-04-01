class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l  = 0
        cur = 0
        longest = 0
        for r in range(len(s)):
            if s[r] in seen:
                seen.remove(s[r])
                l=r

            seen.add(s[r])
            cur = (r-l) + 1
            longest = max(longest , cur)

        return longest


