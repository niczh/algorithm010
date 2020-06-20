#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

#思路 ： 
# 字符串按字节序排序，
# 从最大最小的字符串中取出相同部分
# 即为最长公共前缀。

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs : return ""
        strs = sorted(strs)
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]

# @lc code=end

