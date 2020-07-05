#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0: return False
        if num in [0, 1]: return True
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else :
                left = mid + 1
        return False
# @lc code=end

