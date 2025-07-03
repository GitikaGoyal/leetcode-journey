//Optimized Bit Manipulation Approach
//T.C.->O(log k)
//S.C.->O(1)
#include <bit>
class Solution {
public:
    char kthCharacter(int k) {
        return 'a' + std::popcount(static_cast<unsigned int>(k - 1));
    }
};

//Simulation Approach
//T.C.->O(k)
//S.C.->O(k)
class Solution {
public:
    char kthCharacter(int k) {
        std::vector<int> word;
        word.push_back(0);
        while(word.size() < k)
        {
            int currentSize = word.size();
            for(int i=0; i<currentSize; i++)
            {
                word.push_back((word[i]+1)%26);
            }
        }
        return 'a'+word[k-1];
    }
};
