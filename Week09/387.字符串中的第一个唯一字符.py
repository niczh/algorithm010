#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for c in s:
            dict[c] = dict[c] + 1 if c in dict else 1

        '''
        # solution 1:
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        '''
        # solution 2:
        for k, v in dict.items():
            if v == 1:
                return s.index(k)

        return -1
# @lc code=end

