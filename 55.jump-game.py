#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        if nums[0] == 0: return False
        for n in nums:
            for i in range(1,n):
                if i+nums[i] >= len(nums)-1:
                    return True 
        return False
        
# @lc code=end

