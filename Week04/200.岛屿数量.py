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
            # 将1周边相邻的1都修改为0
            grid[r][c] = 0
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                    dfs(grid, x, y)

        res = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    # 找到一个1就将岛屿计数+1，同时调用dfs将该1毗邻的所有1修改为0
                    res += 1
                    dfs(grid, r, c)

        return res

# @lc code=end

