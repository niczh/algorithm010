/*
 * @lc app=leetcode.cn id=242 lang=cpp
 *
 * [242] 有效的字母异位词
 */

// @lc code=start
class Solution {
public:
    bool isAnagram(string s, string t) {
        // 计数排序
        if (s.size() != t.size()) return false;

        int count[26] = {};

        for (char ch : s) {
            count[ch - 'a'] += 1;
        }
        for (char ch : t) {
            if (count[ch - 'a'] == 0) {
                return false;
            }
            count[ch - 'a'] -=1;
        }
        return true;
    }
};
// @lc code=end

