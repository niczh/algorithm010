#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 采用dict用map的方式实现
        numMap = {}
        for i, num in enumerate(nums):
            if numMap.get(target - num) is not None:
                return [numMap.get(target - num), i]
            numMap[num] = i
# @lc code=end

