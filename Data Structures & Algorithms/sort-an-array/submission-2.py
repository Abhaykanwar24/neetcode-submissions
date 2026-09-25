class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(left , right):
            res = []
            l = 0
            r = 0

            while l < len(left) and r < len(right):
                if left[l] >= right[r]:
                    res.append(right[r])
                    r+=1
                else:
                    res.append(left[l])
                    l+=1

            while l < len(left):
                res.append(left[l])
                l+=1
            while r < len(right):
                res.append(right[r])
                r+=1

            return res


        def merge(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])

            return mergeSort(left , right)


        return merge(nums)