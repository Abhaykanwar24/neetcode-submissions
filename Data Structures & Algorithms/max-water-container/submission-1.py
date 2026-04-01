class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights)-1
        n = len(heights)
        max_area = 0
        while l < r:
            area = min(heights[l] , heights[r]) * (r-l)
            max_area = max(max_area, area)
            if heights[l+1] > heights[l]:
                l+=1
            else:
                r-=1


        return max_area

        