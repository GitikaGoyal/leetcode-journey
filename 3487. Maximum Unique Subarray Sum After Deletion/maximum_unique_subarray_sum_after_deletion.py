#T.C.->O(n)
#S.C.->O(n)

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        total = 0
        max_neg = float('-inf')
        
        for num in nums:
            if num <= 0:
                max_neg = max(max_neg, num)
            elif num not in seen:
                total += num
                seen.add(num)
        
        return max_neg if total == 0 else total
