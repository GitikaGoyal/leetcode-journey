//Approach: Fixed-Size Array
//T.C.-> O(n)
//S.C.->O(n)
class Solution {
public:
    int findLucky(vector<int>& arr) {
        vector<int> count(arr.size() + 1);
        for (const int a : arr)
        {
            if (a <= arr.size())
            count[a]++;
        }
        for (int i = arr.size(); i >= 1; i--)
        {
            if (count[i] == i)
            return i;
        }
        return -1;
    }
};


//Approach: Hash Map
//T.C.-> O(n)
//S.C.-> O(n)
class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int, int> freq;

        // Count frequency
        for (int num : arr) {
            freq[num]++;
        }

        int max_lucky = -1;

        // Check if number == its frequency
        for (auto [num, count] : freq) {
            if (num == count) {
                max_lucky = max(max_lucky, num);
            }
        }

        return max_lucky;
    }
};
