class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = None
        curBest = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:        
                buy = prices[i]
            elif sell is None or prices[i] - buy > curBest:
                sell = prices[i]
                curBest = sell - buy
        return curBest
