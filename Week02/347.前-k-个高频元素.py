#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        pq = []
        for num, freq in freqDict.items():
            if len(pq) < k:
                heapq.heappush(pq, (freq, num))
            elif freq > pq[0][0]:
                heapq.heapreplace(pq, (freq, num))

        res = []
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res

# @lc code=end

