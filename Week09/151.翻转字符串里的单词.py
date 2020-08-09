#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        if not s: return ""
        s = s.split()
        s = s[::-1]
        return ' '.join(s)
# @lc code=end

