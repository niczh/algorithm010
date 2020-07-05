#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if math.isclose(x, 0): return 0.0
        def quickMul(N):
            if N == 0: return 1.0
            half = quickMul(N // 2)
            return half * half if N % 2 == 0 else half * half * x

        if n < 0:
            x = 1 / x
            n = -n
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
# @lc code=end

