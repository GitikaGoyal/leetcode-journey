class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        //result will get stored in subsequences
        int subsequences = 0;
        int min_val = nums[0];
        for(int i=1;i<n;++i){
            if(nums[i]-min_val > k){
                min_val = nums[i];
                subsequences++;
            }
        }
        return subsequences+1;  //last one didnt get count
    }
};

// Time complexity:
// O(nlogn)

// Space complexity:
// O(1)
