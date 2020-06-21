#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        def dfs(grid, r, c):
            grid[r][c] = 0
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                    dfs(grid, x, y)

        res = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    res += 1
                    dfs(grid, r, c)

        return res

# @lc code=end

