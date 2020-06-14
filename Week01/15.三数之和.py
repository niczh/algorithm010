#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        cap = len(nums)
        if (cap < 3):
            return res
        
        nums.sort()
        for i in range(cap - 2):
            if (nums[i] > 0): break
            if (i > 0 and nums[i] == nums[i - 1]): continue
            j = i + 1
            k = cap - 1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if (sum < 0):
                    j += 1
                    while (j < k and nums[j] == nums[j - 1]):
                        j += 1
                elif (sum > 0):
                    k -= 1
                    while (j < k and nums[k] == nums[k + 1]):
                        k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k and nums[j] == nums[j - 1]):
                        j += 1
                    while (j < k and nums[k] == nums[k + 1]):
                        k -= 1
                
        return res

# @lc code=end

