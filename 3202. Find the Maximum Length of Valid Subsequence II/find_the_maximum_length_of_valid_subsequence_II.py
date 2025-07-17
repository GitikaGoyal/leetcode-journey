#Approach - Using LIS Pattern (Bottom Up)
#T.C : O(n^2)
#S.C : O(n*k)
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1 for _ in range(n)] for _ in range(k)]
        max_sub = 1
        #dp[mod][i] keeps track of the longest valid subsequence ending at i with modulo mod
        for i in range(1, n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[mod][i] = max(dp[mod][i], 1 + dp[mod][j])
                max_sub = max(max_sub, dp[mod][i])
        return max_sub
