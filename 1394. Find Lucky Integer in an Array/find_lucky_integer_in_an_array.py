#Approach: Fixed-Size Array
#T.C.-> O(n)
#S.C.->O(n)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [0] * (len(arr) + 1)
        for a in arr:
            if a <= len(arr):
                count[a] += 1
        for i in range(len(arr), 0, -1):
            if count[i] == i:
                return i
        return -1


#Approach: Hash Map
#T.C.-> O(n)
#S.C.-> O(n)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        
        freq = Counter(arr)  # Count frequency
        max_lucky = -1

        for num, count in freq.items():
            if num == count:
                max_lucky = max(max_lucky, num)

        return max_lucky
