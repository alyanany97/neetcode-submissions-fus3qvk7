class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprofit = 0
        lowestprice = prices[0]

        for num in prices:
            lowestprice = min(lowestprice, num)
            maxprofit = max(maxprofit, num - lowestprice)

        
        return maxprofit