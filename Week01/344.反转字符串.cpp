/*
 * @lc app=leetcode.cn id=344 lang=cpp
 *
 * [344] 反转字符串
 */

// @lc code=start
class Solution {
public:
    void reverseString(vector<char>& s) {
        char tmp;
        for (int i = 0, j = s.size() - 1; i < j; ++i, --j) {
            tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
        }
    }
};
// @lc code=end

