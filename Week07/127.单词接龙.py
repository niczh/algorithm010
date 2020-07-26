#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Two-ended BFS
        if endWord not in wordList or len(beginWord) != len(endWord):
            return 0
        front, back = {beginWord}, {endWord}
        dist = 1 # 步数
        wordList = set(wordList)
        word_len = len(beginWord)

        # Two-ended BFS start
        while front and back:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word) # 每个单词用一次保证不会成环
            front = next_front

            if len(back) < len(front):
                front, back = back, front
        
        return 0
# @lc code=end

