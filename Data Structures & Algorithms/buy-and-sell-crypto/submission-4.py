#buy at lowest, sell at highest

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        maxprofit = 0
        lowestprice = prices[0]
        for i in range(len(prices)):
            currentProfit = 0
            lowestprice = min(lowestprice, prices[i])
            difference = prices[i] - lowestprice
            maxprofit = max(maxprofit, difference)
        
        return maxprofit

