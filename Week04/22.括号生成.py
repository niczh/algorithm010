#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ''
        def generate(left, right, n, cur_str):
            # terminator
            if left == n and right == n:
                res.append(cur_str)

            # drill down
            if (left < n):
                generate(left + 1, right, n, cur_str + '(')
            if (right < left):
                generate(left, right + 1, n, cur_str + ')')

            #  reverse states

        generate(0, 0, n, cur)
        return res
# @lc code=end

