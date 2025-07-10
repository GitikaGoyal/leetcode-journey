// Greedy
// T.C.->O(n)
// S.C.->O(n)
class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        vector<int> freeArray; //store durations of free gaps
        //ith event
        //ith start - i-1th end = free gap duration
        freeArray.push_back(startTime[0]);

        for(int i = 1; i < startTime.size(); i++) {
            freeArray.push_back(startTime[i] - endTime[i-1]);
        }

        freeArray.push_back(eventTime - endTime[endTime.size()-1]);

        int n = freeArray.size();
        vector<int> maxRightFree(n, 0);
        vector<int> maxLeftFree(n, 0);
        for(int i = n-2; i >= 0; i--) {
            maxRightFree[i] = max(maxRightFree[i+1], freeArray[i+1]);
        }
        for(int i = 1; i < n; i++) {
            maxLeftFree[i] = max(maxLeftFree[i-1], freeArray[i-1]);
        }

        int result = 0;
        //Iterating on the freeArray
        for(int i = 1; i < n; i++) {
            int currEventTime = endTime[i-1] - startTime[i-1]; //duration of event
            //Case-1 Moving completely out to left or right
            if(currEventTime <= max(maxLeftFree[i-1], maxRightFree[i])) {
                result = max(result, freeArray[i-1] + currEventTime + freeArray[i]);
            }
            //case-2 shift left or right
            result = max(result, freeArray[i-1] + freeArray[i]);
        }

        return result;
    }
};



// Optimized C++ Code (Dynamic maxLeftFree)
// T.C.->O(n)
// S.C.->O(n) → (1 array + 1 temp var)
class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        vector<int> freeArray;

        freeArray.push_back(startTime[0]);

        for (int i = 1; i < startTime.size(); i++) {
            freeArray.push_back(startTime[i] - endTime[i - 1]);
        }

        freeArray.push_back(eventTime - endTime.back());

        int n = freeArray.size();
        vector<int> maxRightFree(n, 0);

        // Precompute maxRightFree only (right-to-left pass)
        for (int i = n - 2; i >= 0; i--) {
            maxRightFree[i] = max(maxRightFree[i + 1], freeArray[i + 1]);
        }

        int result = 0;
        int maxLeft = 0;  // Dynamic maxLeft tracker

        for (int i = 1; i < n; i++) {
            int currEventTime = endTime[i - 1] - startTime[i - 1];

            // Case 1: Replace event with a better free segment
            if (currEventTime <= max(maxLeft, maxRightFree[i])) {
                result = max(result, freeArray[i - 1] + currEventTime + freeArray[i]);
            }

            // Case 2: Remove event, join adjacent free blocks
            result = max(result, freeArray[i - 1] + freeArray[i]);

            // Update maxLeft dynamically
            maxLeft = max(maxLeft, freeArray[i - 1]);
        }

        return result;
    }
};
