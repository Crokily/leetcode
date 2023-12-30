#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy algorithm, the prices are 3 status: front is bigger/smaller than back,or equal.
        # Greedy: Make money every time ,that's the maxProfit, if front is smaller than back,so we can buy in front, sell in back. every time.
        # time complexity: O(n)
        res = 0
        for p in range(1,len(prices)):
            if prices[p-1] < prices[p]:
                res += prices[p]-prices[p-1]
        return res
# @lc code=end

