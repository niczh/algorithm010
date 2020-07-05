#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # BFS
        if (not bank) or (end not in bank) :
            return -1
        chMap = {
            'A' : "CGT",
            'C' : "AGT",
            'G' : "ACT",
            'T' : "ACG"
        }

        queue = [(start, 0)]
        while queue:
            node, step = queue.pop(0)
            if node == end:
                return step
            
            for i, s in enumerate(node):
                for ch in chMap[s]:
                    new_str = node[:i] + ch + node[i+1:]
                    if new_str in bank:
                        queue.append((new_str, step + 1))
                        bank.remove(new_str)

        return -1

        
# @lc code=end

