/*
 * @lc app=leetcode.cn id=739 lang=cpp
 *
 * [739] 每日温度
 */

// @lc code=start
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int len = T.size();
        vector<int> res(len);
        for (int i = len - 1; i >= 0; --i) {
            int j = i + 1;
            while (j < len) {
                if (T[j] > T[i]) {
                    res[i] = j - i;
                    break;
                } else if (res[j] == 0) {
                    break;
                } else {
                    j += res[j];
                }
            }
        }
        return res;
    }
};
// @lc code=end

