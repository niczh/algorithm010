#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
#思路：
#   用字典保存内容，字典key为字典序的字符串，value为字符串list。
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        strDict = {}
        for item in strs:
            tempStr = ''.join(sorted(list(item)))
            if (tempStr in strDict.keys()):
                strDict[tempStr].append(item)
            else:
                strDict[tempStr] = [item]
        
        return list(strDict.values())

# @lc code=end

