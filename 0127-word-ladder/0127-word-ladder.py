class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordList:
            return 0
        queue = deque()
        queue.append((beginWord,1))
        while len(queue)!=0:
            curr, level = queue.popleft()
            if curr == endWord:
                return level
            for i in range(len(curr)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == i:
                        continue
                    new= curr[0:i] + ch + curr[i+1:]
                    if new in wordset:
                        wordset.remove(new)
                        queue.append((new,level +1))
        return 0



                