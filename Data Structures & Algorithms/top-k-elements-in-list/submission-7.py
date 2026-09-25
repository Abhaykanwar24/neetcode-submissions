class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n , 0 ) + 1

        heap = []
        for key in freq:
            heapq.heappush(heap , (freq[key] , key))
            if len(heap) > k:
                heapq.heappop(heap)


        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])


        return res