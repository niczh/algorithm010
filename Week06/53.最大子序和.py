#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        for i in range(1, len(nums)):
            nums[i] += max(0, nums[i-1])
        return max(nums)
# @lc code=end

