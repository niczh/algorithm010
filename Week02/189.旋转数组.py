#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) < 2): return nums

        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()
        return nums
# @lc code=end

