class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_glob = prices[0]
        max_profit = 0
        for ind_sell in range(1,len(prices)):
            max_profit = max(max_profit, prices[ind_sell]-min_glob)
            min_glob = min(min_glob, prices[ind_sell])
        return max_profit

        