#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
'''
#使用set方法实现
 def isAnagram(self, s: str, t: str) -> bool:
        
        setS = set(s)
        res = True
        if setS == set(t):
            for ch in setS:
                res = res and (s.count(ch) == t.count(ch))
        else :
            res = False
        
        return res
'''

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #使用map方法
        if (len(s) != len(t)): 
            return False
        countMap = {}
        for ch in s:
            if ch not in countMap:
                countMap[ch] = 1
            else:
                countMap[ch] += 1
        for ch in t:
            if ch not in countMap:
                return False
            else:
                countMap[ch] -= 1
        
        for item in countMap.values():
            if item != 0:
                return False
        
        return True
# @lc code=end

