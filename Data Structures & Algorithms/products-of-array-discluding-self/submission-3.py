class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        
        # First loop: count zeros + multiply nonzero elements
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zero_count += 1

        if zero_count >= 2:
            return [0] * len(nums)
        
        result = []
        for i in nums:
            if i != 0:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(prod//i)

            else:
                result.append(prod)

        return result


        

