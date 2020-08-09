/*
 * @lc app=leetcode.cn id=300 lang=cpp
 *
 * [300] 最长上升子序列
 */

// @lc code=start
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int len = nums.size();
        if (len == 0) return 0;
        int res = 0;

        vector<int> dp(len, 1);
        for (int i = 1; i<len; ++i) {
            for (int j = i-1; j>=0; --j) {
                if (nums[i] > nums[j]) {
                    dp[i] = (dp[j] + 1) > dp[i] ? (dp[j] + 1) : dp[i];
                    res = (res > dp[i]) ? res : dp[i];
                }
            }
        }
        // 打印vector
        // for (auto i = 0; i != dp.size(); ++i) cout << dp[i] << " ";
        return res;
    }
};
// @lc code=end

