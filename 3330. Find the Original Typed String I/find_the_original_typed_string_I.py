#T.C.->O(n)
#S.C.->O(1)
class Solution:
    def possibleStringCount(self, word: str) -> int:
        frequency = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                frequency += 1
        return frequency
