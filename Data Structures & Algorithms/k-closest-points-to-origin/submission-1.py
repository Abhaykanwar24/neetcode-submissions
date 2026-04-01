class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 
        
        for i, point in enumerate(points):
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, [dist, i])


        res = []
        while k > 0:
            dist , i = heapq.heappop(heap)
            res.append(points[i])
            k-=1

        return res


