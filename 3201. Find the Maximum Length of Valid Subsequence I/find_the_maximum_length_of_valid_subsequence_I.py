#Arrays
#T.C.->O(n)
#S.C.->O(1)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

        # Try building alternating parity subsequence
        alt_len = 1  # At least one number is always included
        prev_parity = nums[0] % 2

        for i in range(1, len(nums)):
            curr_parity = nums[i] % 2
            if curr_parity != prev_parity:
                alt_len += 1
                prev_parity = curr_parity

        return max(count_even, count_odd, alt_len)

      
#Dynamic Programming
#T.C.->O(n)
#S.C.->O(1)
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2
        res = 0
        dp = [[0] * k for _ in range(k)]  # 2x2 DP table initialized with 0

        for i in nums:
            i %= k  # get parity: 0 (even) or 1 (odd)
            for j in range(2):
                dp[j][i] = 1 + dp[i][j]
                res = max(res, dp[j][i])
        
        return res
