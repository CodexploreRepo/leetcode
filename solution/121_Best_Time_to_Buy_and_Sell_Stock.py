class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 0: return max_profit
        buy_price = prices[0]
        for i in range(1, len(prices)):
            if buy_price <= prices[i]:
                max_profit = max(max_profit, prices[i] - buy_price)
            else:
                buy_price = prices[i]
        return max_profit
    
