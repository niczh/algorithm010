#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        i = 0
        j = len(height) - 1
        while (i < j):
            if (height[i] < height[j]) :
                minHeight = height[i]
                i += 1
            else :
                minHeight = height[j]
                j -= 1
            area = minHeight * (j - i + 1)
            max = max if (max > area) else area
        return max
# @lc code=end

