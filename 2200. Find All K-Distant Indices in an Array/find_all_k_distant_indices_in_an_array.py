# T.C.->O(n)
# S.C.->O(1)

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        result = []

        for j in range(n):
            if nums[j] == key:
                start = max(j - k, 0)
                end = min(j + k, n - 1)

                # Avoid duplicate entries by adjusting start
                if result and result[-1] >= start:
                    start = result[-1] + 1

                for i in range(start, end + 1):
                    result.append(i)

        return result
