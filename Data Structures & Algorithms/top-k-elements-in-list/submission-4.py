class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash = {}

        for i in range(len(nums)):
            freq_hash[nums[i]] = 1 + freq_hash.get(nums[i] , 0)

        heap = []
        for key in freq_hash:
            heapq.heappush(heap , (freq_hash[key],key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
