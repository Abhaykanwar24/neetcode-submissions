class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3

        for i in range(len(nums)):
            if nums[i] == 0:
                arr[0] +=1
            elif nums[i] == 1:
                arr[1] +=1

            else:
                arr[2] +=1

       
        index = 0

        for i in range(3):
            for j in range(arr[i]):
                nums[index] = i
                index += 1
