"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Approach -
Create two pointers left and right to find the pair with the maximum difference. Create maxProfit variable to store the maximum difference while 
iterating the poiters through the list like in a time series (from left to right) 


Time complexity - O(n) We only have to scan through out the arrray one time
Space Complexity- O(1)
"""
def maxProfit( prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left,right = 0, 1
        maxProfit = 0

        while right<len(prices):
                #profitable?
                if prices[left] < prices[right]:
                        profit = prices[right]-prices[left]
                        maxProfit = max(maxProfit,profit)
                else:
                        # Because we need to find the maximum difference and
                        #since the right pointer val is now smaller than the left pointer value 
                        # we should assign right to left.
                        left = right
                right += 1
        return maxProfit                






print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
