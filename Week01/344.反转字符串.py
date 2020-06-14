#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(start, end, ls):
            if start >= end:
                return
        
            # swap the first and last element
            ls[start], ls[end] = ls[end], ls[start]        

            return helper(start+1, end-1, ls)
    
        helper(0, len(s)-1, s)
# @lc code=end

