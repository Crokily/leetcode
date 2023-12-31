#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # update the max reach every time
        reach = 0
        for i in range(len(nums)):
            if i > reach: return False
            reach = max(reach,i+nums[i])
        return True

# @lc code=end

