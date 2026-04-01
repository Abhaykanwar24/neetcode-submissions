class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod2 = False
        zero_count = 0
        for i in nums:
            if i != 0:
                if zero_count>=2:
                    prod = 0
                    break
                prod *= i
            else:
                zero_count +=1
                prod2 = True
        
        result = []
        for i in nums:
            if i != 0:
                if prod2:
                    result.append(0)
                else:
                    result.append(prod//i)

            else:
                result.append(prod)

        return result


        

