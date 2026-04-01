class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        l =0 
        r = row*col - 1

        while l<=r:
            mid = (r+l) // 2
            mid_value = matrix[mid//col][mid%col]

            if mid_value == target:
                return True

            elif mid_value < target:
                l+=1
            else:
                r-=1

        return False
               