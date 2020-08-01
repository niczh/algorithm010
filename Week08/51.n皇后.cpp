/*
 * @lc app=leetcode.cn id=51 lang=cpp
 *
 * [51] N皇后
 */

// @lc code=start
class Solution {
// DFS遍历 + 位运算判断冲突
public:
    vector<vector<string>> solveNQueens(int n) {
        if (n < 1) return {};
        size = n;
        mask = (1 << n) - 1;

        vector<int> firstSov(n, 0);
        BT(0, 0, 0, 0, firstSov);

        return generateAns();
    }

private:
    int size, mask;
    vector<vector<int>> resBit;

    void BT(int row, int col, int pie, int na, vector<int> &currSov) {
        // terminator
        if (row == size) {
            resBit.push_back(currSov);
            return;
        }

        int bits = ~(col | pie | na) & mask;
        while (bits) {
            int curr = bits & -bits;
            currSov[row] = curr;
            BT(row + 1, col | curr, (pie | curr) << 1, (na | curr) >> 1, currSov);
            // 还原现场
            bits ^= curr;
        }
    }

    vector<vector<string>> generateAns() {
        vector<vector<string>> res(resBit.size(), vector<string>(size, string(size, '.')));
        for (int i = 0; i < resBit.size(); ++i) {
            for (int j = 0; j < size; ++j) {
                int bitIndex = resBit[i][j];
                int index = 0;
                while (bitIndex) {
                    bitIndex >>= 1;
                    ++index;
                }
                res[i][j][size - index] = 'Q';
            }
        }
        return res;
    }
};
// @lc code=end

