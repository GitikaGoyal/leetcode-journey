// One Time Traversal
// T.C.->O(n)
// S.C.->O(1)

class Solution {
public:
    bool isValid(string word) {
        if(word.size()>=3) {
            bool has_vowel=false;
            bool has_consonant=false;
            for(auto c:word) {
                if(isalpha(c)) {
                    c=tolower(c);
                    if( c=='a' || c=='e' || c=='i' || c=='o' || c=='u') {
                        has_vowel=true;
                    }
                    else
                        has_consonant=true;
                }
                else if(!isdigit(c))
                    return false;
            }
            return has_vowel && has_consonant;
        }
        else
            return false;
    }
};
