class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        l ,r = 0 , len(people) - 1
        while l <= r:
            if people[r] + people[l] <= limit:
                l+=1
            r-=1
            boat+=1        



        return boat