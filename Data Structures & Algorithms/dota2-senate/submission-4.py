class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        count = 0
        
        for n in senate:
            if n == "R":
                if count < 0:
                    senate.append("D")
                count+=1
            else:
                if count > 0:
                    senate.append("R")

                count-=1


        return "Radiant" if count > 0 else "Dire"
                    