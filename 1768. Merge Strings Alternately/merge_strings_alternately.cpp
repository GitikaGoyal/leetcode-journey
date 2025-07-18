//T.C.->O(n+m)
//S.C.->O(n+m)
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";
        int i= 0;
        int j=0;
        while (i < word1.length() && j < word2.length()) {
            result += word1[i];
            result += word2[j];
            i++;
            j++;
        }
        result += word1.substr(i);
        result += word2.substr(j);
        return result;
    }
};
