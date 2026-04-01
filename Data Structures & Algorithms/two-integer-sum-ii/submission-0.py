class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,num in enumerate(numbers):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff]+1 , i+1]
            hash_map[num] = i
        return None        
        