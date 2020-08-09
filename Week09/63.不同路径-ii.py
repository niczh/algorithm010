#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]) + 1)] for _ in range(len(obstacleGrid) + 1)]
        for i in range(1, len(obstacleGrid) + 1):
            for j in range(1, len(obstacleGrid[0]) + 1):
                if i == 1 and j == 1 and obstacleGrid[0][0] != 1:
                    dp[1][1] = 1
                    continue
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else: 
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[len(obstacleGrid)][len(obstacleGrid[0])]
# @lc code=end

