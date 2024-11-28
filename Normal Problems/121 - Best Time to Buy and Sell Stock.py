class Solution:
    def maxProfit(self, prices: List[int]) -> int: # type: ignore
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

########################################### Using Dunamic Programming ################################################

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0  # Tracks the highest profit
#         min_price = prices[0]  # Tracks the lowest price seen so far

#         for current_price in prices:
#             # Calculate profit if sold at current_price
#             max_profit = max(max_profit, current_price - min_price)
#             # Update min_price if current_price is lower
#             min_price = min(min_price, current_price)
        
#         return max_profit
