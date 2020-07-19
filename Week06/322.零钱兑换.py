#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return 0
        max = amount + 1
        dp = [0] + [max] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - coin] if i - coin >= 0 else max for coin in coins]) + 1

        return dp[amount] if dp[amount] < max else -1
        
# @lc code=end

