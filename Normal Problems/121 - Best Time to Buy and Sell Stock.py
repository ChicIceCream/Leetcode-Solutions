class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        # repeat until the sell pointer reaches the end
        while sell < len(prices):
            # checking profit when sell is greater than buy
            if prices[sell] > prices[buy]:
                #calculates the profit
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            # checking when sell is smaller or equal to buy
            else:
                #make buy's value same as sell
                buy = sell
            # and then update the sell
            sell += 1
        
        return max_profit
