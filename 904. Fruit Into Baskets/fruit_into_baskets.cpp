// T.C.->O(n)
// S.C.->O(1)

// Largest Window(subarray) having at most 2 unique type of fruits
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n=fruits.size();
        unordered_map<int,int> mp;
        int i=0;
        int j=0;
        int count=0; //result
        while(j<n)
        {
            mp[fruits[j]]++;
            if(mp.size()<=2)
                count = max(count,j-i+1);
            else{
                mp[fruits[i]]--;
                if(mp[fruits[i]] == 0)
                    mp.erase(fruits[i]);
                i++;
            }
            j++;
        }
        return count;
    }
};
