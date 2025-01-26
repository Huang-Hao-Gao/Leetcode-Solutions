class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        accProfit = 0
        for i in range(len(prices) - 1):
            today = prices[i]
            tom = prices[i + 1]
            if tom > today:
                #buy now then sell tomorrow
                accProfit += tom - today
        return accProfit

        