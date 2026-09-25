class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3

        for n in nums:
            if n == 0:
                freq[0] +=1
            elif n == 1:
                freq[1] +=1
            else:
                freq[2] +=1
        ind = 0
        for i in range(3):
            for j in range(freq[i]):
                nums[ind] = i
                ind += 1
            