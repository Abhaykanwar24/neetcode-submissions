class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        freq_map = {}

        for i in range(len(hand)):
            freq_map[hand[i]] = freq_map.get(hand[i] , 0 ) + 1

        heap = list(freq_map.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0]
            for i in range(start , start + groupSize):
                if freq_map.get(i,0) == 0 :
                    return False
                freq_map[i] -= 1
                if freq_map[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        

        return True