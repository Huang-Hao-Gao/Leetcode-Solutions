class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy, sell variables
        #assign buy to 1st element
        # if next element is greater than cur buy date, make that element the sell date
        # if next element is less than cur buy date, change cur buy date to that element
        # now that both buy and sell date have been initialised:
        # if the following element x: buy < x < sell, ignore it
        # if x > sell, x = sell
        # if x < buy, push it onto a stack where it's the current best buy, but then pop it if there's no better sell option available so that the previous best buy and sell date is preserved
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
