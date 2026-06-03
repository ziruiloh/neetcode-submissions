class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low sell high
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit= max(maxProfit, profit)
            else:
                l = r
            r += 1

        return maxProfit

        #TC = O(n)
        #SC = O(1)

    