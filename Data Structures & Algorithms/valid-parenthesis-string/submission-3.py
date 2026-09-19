class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0   # min / max possible number of unmatched "("
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:                 # "*" can be "(", ")" or empty
                lo -= 1
                hi += 1
            if hi < 0:            # too many ")" even with every * as "("
                return False
            lo = max(lo, 0)       # open count can't go below 0
        return lo == 0            # can we end with zero unmatched "("?