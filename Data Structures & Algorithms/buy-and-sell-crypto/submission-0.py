class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        max_profit = 0
        profit =0 
        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l+=1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit,max_profit)

        return max_profit        
                    


        