class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def Permutation(i):
            if i == len(nums):
                return [[]]

            resPerm = []
            perms = Permutation(i+1)
            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j , nums[i])
                    resPerm.append(pcopy)

            return resPerm

        return Permutation(0)
                    
        