# T.C.->O(n)
# S.C.->O(1)
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mp = defaultdict(int)
        i = 0
        count = 0

        for j in range(n):
            mp[fruits[j]] += 1
            while len(mp) > 2:
                mp[fruits[i]] -= 1
                if mp[fruits[i]] == 0:
                    del mp[fruits[i]]
                i += 1
            count = max(count, j - i + 1)

        return count
