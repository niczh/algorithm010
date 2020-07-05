#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        checkpoint = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= checkpoint:
                checkpoint = i

        return checkpoint == 0
# @lc code=end

