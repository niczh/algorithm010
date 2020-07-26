#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        N = len(M)
        p = [i for i in range(N)]

        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    self._union(p, i, j)

        return len(set([self._parent(p, i) for i in range(N)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            tmp = i
            i = p[i]
            p[tmp] = root
        return root
# @lc code=end

