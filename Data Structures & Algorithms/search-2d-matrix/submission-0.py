class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])
        left,right = 0 , col*row -1

        while left<=right:
            mid = (left+right) // 2
            mid_value = matrix[mid//col][mid%col]

            if mid_value == target:
                return True
            elif target > mid_value:
                left = mid+1
            else:
                right = mid -1

        return False        