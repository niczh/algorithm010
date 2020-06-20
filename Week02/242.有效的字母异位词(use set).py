#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #使用set方法
        setS = set(s)
        res = True
        if setS == set(t):
            for ch in setS:
                res = res and (s.count(ch) == t.count(ch))
        else :
            res = False
        
        return res

# @lc code=end

