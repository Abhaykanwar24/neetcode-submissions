class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}

        for n in hand:
            freq[n] = freq.get(n , 0 ) + 1

        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0]
            for i in range(start , start + groupSize):
                if freq.get(i,0) == 0:
                    return False
                freq[i] -=1
                if freq[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)



        return True
                        