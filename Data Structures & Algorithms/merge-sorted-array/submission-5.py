class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = n - 1
        r = m - 1
        k = m + n  -1


        while l >= 0:
            if r >= 0 and nums1[r] > nums2[l]:
                nums1[k] = nums1[r]
                r -= 1
            else:
                nums1[k] = nums2[l]
                l -= 1

            k -= 1


