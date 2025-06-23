class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0
        cur=nums[0]
        for n in nums:
            if(n-cur)>k:
                res+=1
                cur=n
        return res+1

# Time complexity:
# O(nlogn)

# Space complexity:
# O(1)
