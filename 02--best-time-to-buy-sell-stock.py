class Solution:
    def maxProfit(self, prices):
        profit = 0
        left = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[left]:
                profit = max(profit, prices[i] - prices[left])
            else:
                left = i
        return profit

# Time Complexity (TC): O(n) - We iterate through the 'prices' array once.
# Space Complexity (SC): O(1) - We use a constant amount of extra space for 'profit' and 'left' variables.
