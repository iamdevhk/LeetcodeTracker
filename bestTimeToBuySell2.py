class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        maxProfit=0
        while i+1<len(prices):
            if prices[i+1]-prices[i]>0:
                maxProfit+=prices[i+1]-prices[i]
            i+=1
        return maxProfit
        