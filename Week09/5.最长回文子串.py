#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP
        n = len(s)
        res = ""
        dp = [[0] * n for _ in range(n)]

        # start end
        for start in range(n-1, -1, -1):
            for end in range(start, n):
                if s[start] == s[end]:
                    if end - start < 2:
                        # 单一字符或相邻两字符
                        dp[start][end] = 1
                    else:
                        # 去掉两端相同字符
                        dp[start][end] = dp[start+1][end-1]
                if dp[start][end] == 1 and end - start + 1 > len(res):
                    res = s[start:end+1]

        return res
# @lc code=end

