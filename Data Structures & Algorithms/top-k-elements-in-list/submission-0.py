class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = defaultdict(int) 
        freq = [[] for _ in range(n+1)]
        for n in nums:
            count[n] += 1

        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1 ,0 ,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        