class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        def merge(left , right):
            comb = []
            i = 0 
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    comb.append(left[i])
                    i+=1
                else:
                    comb.append(right[j])
                    j+=1

            while i < len(left):
                comb.append(left[i])
                i+=1 
            while j < len(right):
                comb.append(right[j])
                j+=1 
            return comb 

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            mid = int(len(nums) / 2)
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left , right)


        return merge_sort(nums)