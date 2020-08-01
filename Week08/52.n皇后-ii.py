#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    # DFS + 位运算
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        # terminator
        if row >= n:
            self.count += 1
            return

        bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 当前所有空位

        while bits:
            p = bits & -bits  # 取最低位1放置皇后
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            bits = bits & (bits - 1)  # 放置一个皇后后，最低位的1清零
# @lc code=end

