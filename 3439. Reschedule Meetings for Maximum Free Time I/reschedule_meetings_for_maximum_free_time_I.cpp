// Sliding Window
// T.C.->O(n)
// S.C.->O(n)
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        vector<int> freeArray; // store durations of free gaps
        //free gap duration=ith start - (i-1)th end
        freeArray.push_back(startTime[0]); //starting gap
      
        for(int i=1; i<startTime.size();i++)
        { freeArray.push_back(startTime[i] - endTime[i-1]); }
      
        freeArray.push_back(eventTime - endTime[endTime.size()-1]); //ending gap
      
        //SLIDING WINDOW
        int i=0;
        int j=0;
        int maxSum=0;
        int currSum=0;
        int n=freeArray.size();
        while(j<n) {
            currSum+=freeArray[j];
            if(i< n && j-i+1 > k+1) { //k+1 is window size
                currSum-=freeArray[i];
                i++;
            }
            maxSum=max(maxSum,currSum);
            j++;
        }
        return maxSum;
    }
};

//Prefix-Sum
//T.C.->O(n)
//S.C.->O(n)
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size(), res = 0;
        vector<int> sum(n + 1);
        for (int i = 0; i < n; i++) {
            sum[i + 1] = sum[i] + endTime[i] - startTime[i];
        }
        for (int i = k - 1; i < n; i++) {
            int right = i == n - 1 ? eventTime : startTime[i + 1];
            int left = i == k - 1 ? 0 : endTime[i - k];
            res = max(res, right - left - (sum[i + 1] - sum[i - k + 1]));
        }
        return res;
    }
};
