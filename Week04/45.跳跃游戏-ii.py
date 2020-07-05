#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        res, fur, end = 0, 0, 0
        for i in range(len(nums) - 1):
            if fur >= i:
                fur = max(fur, nums[i] + i)
                if i == end:
                    end = fur
                    res += 1
        return res
# @lc code=end

