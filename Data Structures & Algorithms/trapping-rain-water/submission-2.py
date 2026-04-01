from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r = 0 , len(height) -1
        max_left = height[l]
        max_right = height[r]
        water = 0

        while l < r :
            if height[l] < height[r]:
                l+=1
                max_left = max(height[l] , max_left)
                water += max_left - height[l]
            else:
                r-=1
                max_right = max(height[r] , max_right)
                water += max_right - height[r]   

        return water