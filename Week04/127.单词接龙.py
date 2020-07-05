#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = collections.deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                letters = list(word)
                for i in range(word_len):
                    origin_char = letters[i]

                    for j in range(26):
                        letters[i] = chr(ord('a') + j)
                        new_word = ''.join(letters)
                        if new_word in word_set:
                            if new_word == endWord:
                                return step + 1
                            if new_word not in visited:
                                queue.append(new_word)
                                visited.add(new_word)
                    # 还原现场
                    letters[i] = origin_char
            step += 1
        return 0

# @lc code=end

