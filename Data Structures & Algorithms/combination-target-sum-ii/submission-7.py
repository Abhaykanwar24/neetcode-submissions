class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res_comb = []
        cur_comb = []


        def backtrack(i , cur_sum):
            if cur_sum == target:
                res_comb.append(cur_comb.copy())
                return 
            if i >= len(candidates) or cur_sum > target:
                return

            cur_comb.append(candidates[i])
            backtrack(i+1 , candidates[i] + cur_sum)
            cur_comb.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            backtrack(i+1 , cur_sum)


        backtrack(0 , 0 )

        return res_comb
        