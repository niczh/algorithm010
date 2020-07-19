#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(m)] 
        for i in range(1, n): s
            for j in range(1, m): 
                dp[j] += dp[j - 1]
        return dp[m - 1]
# @lc code=end

