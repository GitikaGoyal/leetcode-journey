//T.C.->O(n)
//S.C.->O(n)
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = *max_element(candies.begin(), candies.end());
        vector<bool> result;

        for (int curNum : candies) {
            result.push_back(curNum + extraCandies >= maxCandies);
        }

        return result;
    }
};
