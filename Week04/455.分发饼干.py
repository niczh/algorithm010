#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s: 
            return 0
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
            
        return res
        
        
# @lc code=end

