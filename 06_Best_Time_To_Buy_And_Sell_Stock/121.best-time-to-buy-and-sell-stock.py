#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # #! method 1:
        # #? using a double for loop O(n^2)
        # #? scan though the list twice and find the max profit
        # max_profit = 0
        # for i_idx, first in enumerate(prices[:-1]):
        #     for second in prices[i_idx + 1:]:
        #         if second - first > max_profit:
        #             max_profit = second - first
        # return max_profit
        # #* this method will get very slow if the list is long
        # #* would be even worse if we didn't use list slicing
        #! method 2:
        #? using 2 pointers, O(n)
        #? we put one at the beginning and one 1 day ahead
        #? if the price is lower than the first pointer, we update the first pointer
        #? if the price is higher than the second pointer, we update the second pointer
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            #? is it profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit
# @lc code=end
