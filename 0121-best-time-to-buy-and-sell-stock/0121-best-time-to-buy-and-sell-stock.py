class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit=  float("-inf")
        for i in  range (0, len(prices)):
            buy = min(buy, prices[i])
            diff = prices[i] - buy
            profit = max(diff, profit)

        return profit

        