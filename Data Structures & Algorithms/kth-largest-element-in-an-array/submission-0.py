class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-s for s in nums]

        heapq.heapify(minHeap)

        while k-1 > 0:
            heapq.heappop(minHeap)
            k-=1

        return -minHeap[0]


        