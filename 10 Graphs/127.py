import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0

        graph = collections.defaultdict(list)

        for word in wordList:  # O(N), where N is the number of words
            for i in range(len(word)):  # O(M), where M is the length of the word
                transform = word[:i] + "*" + word[i+1:]  # O(M)
                graph[transform].append(word)

        # O(M^2) * O(N)
        queue = collections.deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, distance = queue.popleft()

            if word == endWord:
                return distance

            visited.add(word)

            for i in range(len(word)):
                transformed = word[:i] + "*" + word[i+1:]
                potential_words = graph.get(transformed, None)

                if potential_words:
                    for potential_word in potential_words:
                        if potential_word not in visited:
                            queue.append((potential_word, distance + 1))

        return 0

a = Solution()
print(a.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5