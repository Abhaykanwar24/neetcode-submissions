class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        max_num = 0
        for r in range(k-1 , len(nums)):
            i=l
            while i <= r:
                max_num = max(nums[i] , max_num)
                i+=1
            res.append(max_num)
            l+=1  

        return res      

        