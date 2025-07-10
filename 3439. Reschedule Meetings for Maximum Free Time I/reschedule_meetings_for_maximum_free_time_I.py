# Sliding Window
# T.C.->O(n)
# S.C.->O(n)
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeArray = []
        # Starting gap
        freeArray.append(startTime[0])
        # In-between free gaps
        for i in range(1, len(startTime)):
            freeArray.append(startTime[i] - endTime[i - 1])
        # Ending gap
        freeArray.append(eventTime - endTime[-1])
        # Sliding window of size k+1 over freeArray
        i = 0
        j = 0
        currSum = 0
        maxSum = 0
        n = len(freeArray)
        while j < n:
            currSum += freeArray[j]
            if j - i + 1 > k + 1:
                currSum -= freeArray[i]
                i += 1
            maxSum = max(maxSum, currSum)
            j += 1
        return maxSum



#Prefix-Sum
#T.C.->O(n)
#S.C.->O(n)
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        total = [0] * (n + 1)
        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]
        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
        return res
