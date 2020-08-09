#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口
        target_len = len(p)
        source_len = len(s)
        if target_len * source_len == 0 or target_len > source_len:
            return []

        res = []
        p_count, s_count = [0] * 26, [0] * 26
        for ch in p:
            p_count[ord(ch) - 97] += 1

        left = 0
        for right in range(source_len):
            s_count[ord(s[right]) - 97] += 1
            if right < target_len - 1:
                # 尚未达到窗口长度
                continue
            # 达到窗口长度
            if p_count == s_count:
                res.append(left)
            # 移出左边一个字符
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res
# @lc code=end

