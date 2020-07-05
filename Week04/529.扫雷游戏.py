#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        r, c = len(board), len(board[0])
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        def cal(i, j):
            # 计算周围炸弹数
            counter = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0: continue
                    if 0 <= i + x < r and 0 <= j + y < c \
                        and board[i + x][j + y] == 'M':
                        counter += 1
            return counter

        def bfs(i, j):
            queue = collections.deque()
            queue.append([i, j])
            while queue:
                i, j = queue.pop()
                num = cal(i, j)
                if num > 0:
                    board[i][j] = str(num)
                    continue
                board[i][j] = 'B'
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0: continue
                        new_i, new_j = i + x, j + y
                        if new_i < 0 or new_i >= r or \
                            new_j < 0 or new_j >= c:
                            continue
                        if board[new_i][new_j] == 'E':
                            queue.appendleft([new_i, new_j])
                            board[new_i][new_j] = "B"

        bfs(i, j)
        return board
# @lc code=end

