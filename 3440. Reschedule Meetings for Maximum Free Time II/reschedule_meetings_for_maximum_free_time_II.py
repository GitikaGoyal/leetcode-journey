# Greedy
# T.C.->O(n)
# S.C.->O(n)
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        freeArray = []
        freeArray.append(startTime[0])
        for i in range(1, len(startTime)):
            freeArray.append(startTime[i] - endTime[i - 1])
        freeArray.append(eventTime - endTime[-1])

        n = len(freeArray)
        maxRightFree = [0] * n
        maxLeftFree = [0] * n
        for i in range(n - 2, -1, -1):
            maxRightFree[i] = max(maxRightFree[i + 1], freeArray[i + 1])
        for i in range(1, n):
            maxLeftFree[i] = max(maxLeftFree[i - 1], freeArray[i - 1])

        result = 0
        for i in range(1, n):
            # Duration of the event between freeArray[i-1] and freeArray[i]
            currEventTime = endTime[i - 1] - startTime[i - 1]

            # Case 1: Entire event can be shifted to a large free block completely out
            if currEventTime <= max(maxLeftFree[i - 1], maxRightFree[i]):
                result = max(result, freeArray[i - 1] + currEventTime + freeArray[i])

            # Case 2: Event is removed, only the two adjacent free blocks are combined when shifted only left or right
            result = max(result, freeArray[i - 1] + freeArray[i])

        return result
 



# Optimized C++ Code (Dynamic maxLeftFree)
# T.C.->O(n)
# S.C.->O(n) → (1 array + 1 temp var)
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        freeArray = []
        freeArray.append(startTime[0])
        for i in range(1, len(startTime)):
            freeArray.append(startTime[i] - endTime[i - 1])
        freeArray.append(eventTime - endTime[-1])

        n = len(freeArray)
        maxRightFree = [0] * n
        for i in range(n - 2, -1, -1):
            maxRightFree[i] = max(maxRightFree[i + 1], freeArray[i + 1])

        result = 0
        maxLeft = 0  # Running max from the left side

        for i in range(1, n):
            currEventTime = endTime[i - 1] - startTime[i - 1]

            # Case 1: Remove event and fill it with a longer free block elsewhere
            if currEventTime <= max(maxLeft, maxRightFree[i]):
                result = max(result, freeArray[i - 1] + currEventTime + freeArray[i])

            # Case 2: Just remove event and join the two free intervals
            result = max(result, freeArray[i - 1] + freeArray[i])

            # Dynamically update maxLeft
            maxLeft = max(maxLeft, freeArray[i - 1])

        return result
 
