/*
 * @lc app=leetcode.cn id=62 lang=cpp
 *
 * [62] 不同路径
 */

// @lc code=start
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m <= 0 || n <= 0) return 0;
        if (m == 1 || n == 1) return 1;

        vector<vector<int> > dp(m+1, vector<int>(n+1, 0));
        dp[1][1] = 1;
        for (int i = 1; i < m+1; ++i) {
            for (int j = 1; j < n+1; ++j) {
                if (i == 1 && j == 1) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return dp[m][n];
    }
};
// @lc code=end

