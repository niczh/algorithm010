#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i, num5, num10 = 0, 0, 0
        for bill in bills:
            if bill == 5:
                num5 += 1
            elif bill == 10:
                num5 -= 1
                num10 += 1
            elif bill == 20:
                if num10 == 0:
                    num5 -= 3
                else:
                    num10 -= 1
                    num5 -= 1
            else:
                return False
            if num5 < 0:
                return False

        return True
# @lc code=end

