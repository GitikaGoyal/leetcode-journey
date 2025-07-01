//T.C.->O(n)
//S.C.->O(1)
class Solution {
public:
    int possibleStringCount(string word) {
         int frequency = 1; 

        for (int i = 1; i < word.size(); ++i) {
   
            frequency += (word[i] == word[i - 1]);
        }
      
        // Return the final frequency count
        return frequency;
    }
};
