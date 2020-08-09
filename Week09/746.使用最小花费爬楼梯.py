#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        leng = len(cost)
        if leng == 0: return 0
        if leng == 1: return cost[0]
        prev, last, curr = cost[0], cost[1], 0
        for i in range(2, leng):
            curr = min(prev, last) + cost[i]
            prev, last = last, curr

        return min(prev, last)
        
# @lc code=end

