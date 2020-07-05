#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = [[]]
        for i in nums:
            res += [item + [i] for item in res]
        return res
# @lc code=end

