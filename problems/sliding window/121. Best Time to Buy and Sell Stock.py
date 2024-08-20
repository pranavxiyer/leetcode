# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# difficulty: easy

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit