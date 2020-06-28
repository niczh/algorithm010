/*
 * @lc app=leetcode.cn id=22 lang=cpp
 *
 * [22] 括号生成
 */

// @lc code=start
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if (n == 0) return res;
        generate(0, 0, n, "");
        return res;
    }
private:
    vector<string> res;
    string s;
    void generate(int left, int right, int n, string currStr){
        if (left == n && right == n) {
            res.push_back(currStr);
            return;
        }
        if (left < n) {
            generate(left + 1, right, n, currStr + '(');
        }
        if (right < left) {
            generate(left, right + 1, n, currStr + ')');
        }
    }
};
// @lc code=end

