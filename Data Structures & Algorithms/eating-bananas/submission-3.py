class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            total_time =0
            for pile in piles:
                total_time += math.ceil(pile / speed)

            if total_time <=h:
                return speed

            speed +=1

        return speed

        