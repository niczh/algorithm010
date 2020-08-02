/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        int length = intervals.size();
        if (length == 0) {
            return {};
        }
        sort(intervals.begin(), intervals.end());
        int left = intervals[0][0];
        int right = intervals[0][1];
        for (int i = 1; i < length; ++i) {
            if (intervals[i][0] <= right) {
                if (intervals[i][1] > right) {
                    right = intervals[i][1];
                }
            } else {
                res.push_back({left, right});
                left = intervals[i][0];
                right = intervals[i][1];
            }
        }
        res.push_back({left, right});
        
        return res;    
    }
};
// @lc code=end

