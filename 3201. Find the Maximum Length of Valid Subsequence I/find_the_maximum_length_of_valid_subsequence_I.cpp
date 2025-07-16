//Arrays
//T.C.->O(n)
//S.C.->O(1)
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        //The possible sequence either contains all even elements, all odd elements, alternate even odd, or alternate odd even elements. 
        //sub[i]   sub[i+1]     %2
        //even     even         0
        //odd      odd          0
        //even     odd          1
        //odd      even         1
        //Considering only the parity of elements, there are only 4 possibilities and we can try all of them.
        
        int countEven = 0, countOdd = 0;
        for (int num : nums) {
            if (num % 2 == 0) countEven++;
            else countOdd++;
        }
        // Try building alternating parity subsequence
        int altLen = 1; // At least one number
        int prevParity = nums[0] % 2;

        for (int i = 1; i < nums.size(); ++i) {
            int currParity = nums[i] % 2;
            if (currParity != prevParity) {
                altLen++;
                prevParity = currParity;
            }
        }
        return max({countEven, countOdd, altLen});
    }
};

//Dynamic Programming
//T.C.->O(n)
//S.C.->O(1)
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int n = nums.size(),k = 2, res = 0;
        vector<vector<int>> dp(k,vector<int> (k,0));

        for(auto i:nums)
        {
            i %= k;
            for(int j = 0 ;j < 2;j++)
            {
                dp[j][i] = 1 + dp[i][j];
                res = max(res, dp[j][i]);
            }
        }
        return res;
    }
};
