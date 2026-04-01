class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k == 1:
            return nums[:]


        output = []
        q = deque()
        l=r=0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(nums[r])

            if r - l + 1 > k:
                if q and q[0] == l:
                    q.popleft()
                l += 1

            if r - l + 1 == k:
                output.append(nums[q[0]])
            

            r+=1


        return output
            
            

            