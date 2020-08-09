/*
 * @lc app=leetcode.cn id=198 lang=cpp
 *
 * [198] 打家劫舍
 */

// @lc code=start
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];

        int len = nums.size();
        vector<int> dp(len+1, 0);
        dp[1] = nums[0];
        for (int i = 2; i < len+1; ++i) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
        }
        return dp[len];
    }
};
// @lc code=end

