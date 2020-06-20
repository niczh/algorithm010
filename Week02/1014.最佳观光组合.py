#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxScore = 0
        maxJ = A[-1] - len(A) + 1
        for i in range(len(A) - 2, -1, -1):
            maxScore = max(maxScore, A[i] + i + maxJ)
            maxJ = max(maxJ, A[i] - i)

        return maxScore
# @lc code=end

