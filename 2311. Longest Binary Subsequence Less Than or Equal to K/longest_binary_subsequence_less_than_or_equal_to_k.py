class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n=len(s)
        length = 0
        powerValue = 1
        
        for i in range(n-1,-1,-1): 
            if (s[i] == '0'): 
                length+=1
            elif(powerValue <= k): 
                length+=1
                k -= powerValue
                
            if (powerValue <= k):
                powerValue <<= 1 #powerValue *= 2
        return length
